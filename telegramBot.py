from telegram import  Bot
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_KEY")
CHAT_ID = os.getenv("CHAT_ID")
async def sending_message(message):

    bot=Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID,text=message)
    # first time I hear about async and await in python --- pretty weird.
# asyncio.run(sending_message("Hello from my bot!"))