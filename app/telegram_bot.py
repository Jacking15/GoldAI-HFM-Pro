from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from app.config import Config

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 GoldAI HFM Pro Aktif\n\nKetik /signal untuk analisis XAUUSD\nKetik /status untuk info bot"
    )

# STATUS
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = f"""
📊 STATUS BOT

Symbol: {Config.SYMBOL}
Mode: {Config.MODE}
Risk: {Config.RISK_PERCENT}%
Timeframe: {','.join(Config.TIMEFRAMES)}
"""
    await update.message.reply_text(msg)

# SIGNAL (dummy dulu)
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Analisis sementara...\n\nBUY: 70%\nSELL: 30%\n\n(Engine akan aktif di Sprint 2)"
    )

def run_bot():
    app = ApplicationBuilder().token(Config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("signal", signal))

    print("Bot running...")
    app.run_polling()