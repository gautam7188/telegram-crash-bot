import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Crash Predictor Bot!\nUse /predict to get the next multiplier.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    multiplier = round(random.uniform(1.2, 5.0), 2)
    await update.message.reply_text(f"📊 Predicted crash multiplier: x{multiplier}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    print("🚀 Bot is running...")
    app.run_polling()
