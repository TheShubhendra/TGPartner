#!/usr/bin/python
# A telegram bot that works parallel with you
# and provide additional interface and unlimited features.
# Copyright (C) 2021 Shubhendra Kushwaha
# @TheShubhendra shubhendrakushwaha94@gmail.com
# This file is a part of TGPartner <https://github.com/TheShubhendra/TGPartner>.
#
# TGPartner is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TGPartner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TGPartner.  If not, see <http://www.gnu.org/licenses/>.
import asyncio
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession

from tgpartner.config import (
    ENV,
    APP_ID,
    API_HASH,
    STRING_SESSION,
    LOGGING_LEVEL,
)
from tgpartner.bootloader import (
    send_success_message,
    load_plugins,
    load_core_files,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(message)s",
    level=LOGGING_LEVEL,
)
logger = logging.getLogger()


async def start(client):
    await load_core_files(client)
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
