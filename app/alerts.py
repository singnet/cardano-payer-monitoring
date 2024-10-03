import requests
import json
from logger import logger
from config import MATTERMOST_URL, scan_link


def send_notification(payer_data, balance, status: str):

    message = f"##### 🚨 Payer balance level alert - {status} 🚨 \n"

    message += f'| Token Payer | Balance | Nodes | Address |\n'
    message += f'| :------------: |:-----------:|:-------------:|:----|\n'
    message += f'| {payer_data["token_payer"]} | {balance} ADA | {payer_data["nodes"]} | [{payer_data["mask_address"]}]({scan_link}{payer_data["address"]}) |\n'

    headers = {"Content-Type": "application/json"}
    payload = {"text": message}
    response = requests.post(MATTERMOST_URL, headers=headers, data=json.dumps(payload))
    logger.info(f"Mattermost response [code {response.status_code}]: {response.text}")


def send_bulk_notification(payers_data):
    message = f"##### 📣 Daily Payers Report 📣 \n"
    message += f'| Token Payer | Balance | Nodes | Address |\n'
    message += f'| :------------: | :-----------: | :-------------: | :----: | :----: |\n'

    for payer in payers_data:
        message += f'| {payer["token_payer"]} | {payer["balance"]} ADA | {payer["nodes"]} | [{payer["mask_address"]}]({scan_link}{payer["address"]}) |\n'

    headers = {"Content-Type": "application/json"}
    payload = {"text": message}
    response = requests.post(MATTERMOST_URL, headers=headers, data=json.dumps(payload))
    logger.info(f"Daily Report :: mattermost response [code {response.status_code}]: {response.text}")






