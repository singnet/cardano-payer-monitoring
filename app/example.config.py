from constants import TokenPayer
from enum import Enum
import pytz

MATTERMOST_URL = ""

BLOCKFROST_API_KEY = '<API_KEY>'

during_day_interval = 60  # minutes


class MorningTimeAlert(Enum):
    HOURS = 10
    MINUTES = 00


class EveningTimeAlert:
    HOURS = 18
    MINUTES = 00


timezone = pytz.timezone('<TIMEZONE>')

node_one = ""
node_two = ""

scan_link = "https://cardanoscan.io/address/"

PAYERS = [
    {
        "mask_address": "addr1qxm66dha...abcd",
        "address": "full address",
        "token_payer": TokenPayer.<TOKEN_NAME>.value,
        "nodes": f"<NODES DISCRIPtIONS>)"
    }
]


