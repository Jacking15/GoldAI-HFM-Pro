import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    MODE = os.getenv("MODE", "SIGNAL")
    RISK_PERCENT = float(os.getenv("RISK_PERCENT", 1))

    SYMBOL = os.getenv("SYMBOL", "XAUUSD")
    TIMEFRAMES = os.getenv("TIMEFRAMES", "M1,M5,M15").split(",")
