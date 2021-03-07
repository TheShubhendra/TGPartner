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
import asyncio


AFK_ACTIVATED = False
AFK_MESSAGE = " "


@client.on(events.NewMessage(incoming=True, func=lambda x: x.is_private or x.mentioned))
async def handle_afk(event):
    if AFK_ACTIVATED:
        await event.reply(f"I am AFK reason: {AFK_MESSAGE}")


@client.on(events.NewMessage(outgoing=True))
async def remove_afk(event):
    global AFK_ACTIVATED
    if not AFK_ACTIVATED:
        return
    if ",afk" in event.text:
        await event.edit(event.text.replace(",afk",""))
        return
    await event.respond("Afk deactivated")
    AFK_ACTIVATED = False


@client.on(events.NewMessage(outgoing=True, pattern="\.afk (.*)"))
async def activate_afk(event):
    global AFK_ACTIVATED, AFK_MESSAGE
    AFK_ACTIVATED = True
    AFK_MESSAGE = event.pattern_match.group(1)
    await event.edit(f"Activating AFK reason: {AFK_MESSAGE}")
    await asyncio.sleep(2)
    await event.delete()
