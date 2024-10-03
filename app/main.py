from fastapi import FastAPI
from blockfrost import BlockFrostApi, ApiError
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from contextlib import asynccontextmanager
from logger import logger

from config import timezone, during_day_interval, BLOCKFROST_API_KEY, PAYERS
from constants import BalanceValue, AddressHealth
from alerts import send_notification, send_bulk_notification

blockfrost_api = BlockFrostApi(project_id=BLOCKFROST_API_KEY)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        check_balances,
        "interval",
        minutes=during_day_interval
    )
    # morning
    scheduler.add_job(
        send_daily_balances,
        CronTrigger(hour=10, minute=00, timezone=timezone)
    )
    # evening
    scheduler.add_job(
        send_daily_balances,
        CronTrigger(hour=18, minute=00, timezone=timezone)
    )
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


async def check_balances() -> None:
    logger.info("Checking balances ... ")
    for payer_data in PAYERS:
        try:
            address_info = blockfrost_api.address(payer_data["address"])
            balance = sum([int(amount.quantity) for amount in address_info.amount if amount.unit == "lovelace"])
            ada_balance = balance / 1_000_000
            logger.info(f"Balance for {payer_data['address']}: {ada_balance} ADA")

            balance_health(payer_data, ada_balance)

        except ApiError as e:
            logger.info(f"Error for get balance {payer_data['address']}: {str(e)}")


async def send_daily_balances() -> None:
    for payer_data in PAYERS:
        try:
            address_info = blockfrost_api.address(payer_data["address"])
            balance = sum([int(amount.quantity) for amount in address_info.amount if amount.unit == "lovelace"])
            ada_balance = balance / 1_000_000
            logger.info(f"Balance for {payer_data['address']}: {ada_balance} ADA")
            payer_data["balance"] = ada_balance

        except ApiError as e:
            logger.info(f"Error for get balance {payer_data['address']}: {str(e)}")

    send_bulk_notification(PAYERS)


def balance_health(payer_data, address_balance):
    rounded_balance = round(address_balance)
    if rounded_balance <= BalanceValue.MEDIUM.value:
        balance_status = AddressHealth.MEDIUM.value
    elif rounded_balance <= BalanceValue.LOW.value:
        balance_status = AddressHealth.LOW.value
    elif rounded_balance < BalanceValue.CRITICAL.value:
        balance_status = AddressHealth.CRITICAL.value
    else:
        balance_status = AddressHealth.NORMAL.value

    if balance_status != AddressHealth.NORMAL.value:
        send_notification(payer_data, address_balance, balance_status)
        logger.info(f"Balance Health notification sent for {payer_data}")
