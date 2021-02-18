import asyncio
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession

from tgpartner.config import (
    ENV,
    APP_ID,
    API_HASH,
    STRING_SESSION,
)
from tgpartner.bootloader import (
    send_success_message,
    load_plugins,
    )

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger()


async def start(client):
    await load_plugins(client)
    await send_success_message(client)

async def main():
    logger.info(f"Starting bot in {ENV} environment.")
    if ENV == "production":
        client = TelegramClient(StringSession(STRING_SESSION), APP_ID, API_HASH)
    else:
        client = TelegramClient("TGPartner", APP_ID, API_HASH)
    await client.start()
    logger.info("Bot has been started.")
    await start(client)
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
