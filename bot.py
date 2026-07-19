from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "PASTE_YOUR_NEW_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your bot is working.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
