from enum import Enum


class AddressHealth(Enum):
    MEDIUM = "⛽ Medium payer balance (Need a deposit)"
    LOW = "⚠️ Low payer balance"
    CRITICAL = "🆘 CRITICAL Low payer balance"
    NORMAL = "OK BALANCE"


class BalanceValue(Enum):
    MEDIUM = 200000000
    LOW = 100000000
    CRITICAL = 50000000


class TokenPayer(Enum):
    AGIX = "AGIX"
    NTX = "NTX"
    RJV = "RJV"
    CGV = "CGV"
    WMTX = "WMTX"
    FET = "FET"
