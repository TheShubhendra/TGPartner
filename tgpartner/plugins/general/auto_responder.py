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
from telethon.sync import events
from decouple import config

AUTO_RESPOND = bool(int(config("AUTO_RESPOND", 0)))
AUTO_RESPOND_DB = {
    "good morning": "Good Morning",
    "hi": "Hello",
    "hello": "Hi",
    "hlw": "Hii",
    "morning": "Morning",
    "morno": "Morning",
    "good night": "Good Night, Take care",
    "hey": "Yoooo",
}


@client.on(
    events.NewMessage(
        incoming=True,
        outgoing=False,
        func=lambda e: (e.is_private or e.mentioned) and AUTO_RESPOND,
    )
)
async def auto_respond(event):
    if event.fwd_from:
        return
    text = event.text.lower()
    for message in AUTO_RESPOND_DB.keys():
        if message in text:
            await event.reply(AUTO_RESPOND_DB[message])
            return
