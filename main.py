import os
from dotenv import load_dotenv
from telethon import TelegramClient
import asyncio
from ChannelParser import ChannelParser
from database.models.AlchemyCore import AlchemyCore

#load env file
load_dotenv()

# Telegram app credentials
api_hash = os.getenv('API_HASH')
api_id = os.getenv('API_ID')

async def run():
    async with TelegramClient('anon', api_id, api_hash) as client:
        #instantiate sqlalchemy module
        core = AlchemyCore()

        #start parser
        cp = ChannelParser("",  client, core)
        await cp.get_channel_pinned_group()

if __name__ == '__main__':
    asyncio.run(run())


