import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("8727899215:AAE_QzyzgEg-O0bcN-6DVb5YvKuTqSQmcD4")
    TELEGRAM_CHAT_ID = os.getenv("TrenSignal_Bot")

    MODE = os.getenv("MODE", "SIGNAL")
    RISK_PERCENT = float(os.getenv("RISK_PERCENT", 1))

    SYMBOL = os.getenv("SYMBOL", "XAUUSD")
    TIMEFRAMES = os.getenv("TIMEFRAMES", "M1,M5,M15").split(",")
