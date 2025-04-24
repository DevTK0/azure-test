import sys
from telegram import Bot
from dotenv import load_dotenv
import asyncio

import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://test-aisgbot.azurewebsites.net/api/telegram-webhook"

async def setup_webhook():
    
    print("Setting up webhook...")
    bot = Bot(token=BOT_TOKEN)
    
    # Remove any existing webhook
    await bot.delete_webhook()
    
    # Set new webhook
    success = await bot.set_webhook(url=WEBHOOK_URL)
    
    if success:
        print(f"✅ Webhook was set successfully to URL: {WEBHOOK_URL}")
    else:
        print("❌ Failed to set webhook")
        
    # Print webhook info for verification
    webhook_info = await bot.get_webhook_info()
    print(f"Current webhook status: {webhook_info}")

if __name__ == "__main__":
    asyncio.run(setup_webhook())
