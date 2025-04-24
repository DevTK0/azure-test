import azure.functions as func

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import numpy as np

from dotenv import load_dotenv
import logging


import os


load_dotenv()

app = func.FunctionApp()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello world")


@app.route(route="telegram-webhook", auth_level=func.AuthLevel.ANONYMOUS)
async def telegram_webhook(req: func.HttpRequest) -> func.HttpResponse:
    request_body = {
        "update_id": 1,
        "message": {
            "message_id": 123,
            "from": {
                "id": 456,
                "is_bot": False,
                "first_name": "Test",
                "username": "testuser",
            },
            "chat": {
                "id": 456,
                "first_name": "Test",
                "username": "testuser",
                "type": "private",
            },
            "date": 1714465532,  # You'll need to replace this with the actual timestamp
            "text": "Hello bot!",
        },
    }

    bot = Application.builder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    await bot.initialize()

    await bot.process_update(Update.de_json(request_body, bot.bot))
    await bot.shutdown()

    return func.HttpResponse("OK")
