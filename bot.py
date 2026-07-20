from telegram import Update
import os
 from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your bot is working.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
