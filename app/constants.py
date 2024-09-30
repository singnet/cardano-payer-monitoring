from enum import Enum


class AddressHealth(Enum):
    MEDIUM = "⛽ Medium payer balance (Need a deposit)"
    LOW = "⚠️ Low payer balance"
    CRITICAL = "🆘 CRITICAL Low payer balance"
    NORMAL = "OK BALANCE"


class BalanceValue(Enum):
    MEDIUM = 150
    LOW = 100
    CRITICAL = 50


class TokenPayer(Enum):
    AGIX = "AGIX"
    NTX = "NTX"
    RJV = "RJV"
    CGV = "CGV"
    WMTX = "WMTX"
    FET = "FET"
