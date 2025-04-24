import azure.functions as func
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

import os

load_dotenv()

app = func.FunctionApp()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello world")

@app.route(route="test", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("hello world")

# @app.route(route="telegram-webhook", auth_level=func.AuthLevel.ANONYMOUS)
# async def telegram_webhook(req: func.HttpRequest) -> func.HttpResponse:
    
#     request_body = req.get_json()
    
#     bot = Application.builder().token(BOT_TOKEN).build()
#     bot.add_handler(CommandHandler("start", start))
    
#     await bot.process_update(Update.de_json(request_body, bot.bot))
#     await bot.shutdown()
    
#     return func.HttpResponse("OK")
