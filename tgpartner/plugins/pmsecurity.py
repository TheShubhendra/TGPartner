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
from telethon.sync import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import (
    BlockRequest,
    UnblockRequest,
)

from tgpartner.database import pmsecurity_api as api
from tgpartner.config import LOGGING_GROUP

WARNS = dict()
MAX_WARNS = 3

BLOCKING_TEXT = "Your have crossed the limit..So PM security is going to block you. Your all messages , chat_is has been logged successfully, no matter if you have deleted those."
WARNING_TEXT = "Welcome to the PMSecurity system of TGPartner. You are not verified yet, so wait for my master, and don't try to spam , otherwise you will be blocked automatically."


@client.on(
    events.NewMessage(incoming=True, outgoing=False, func=lambda e: e.is_private)
)
async def check_approval(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    if api.is_approved(event.chat_id):
        return
    if chat_id not in WARNS.keys():
        WARNS[chat_id] = 0
    else:
        WARNS[chat_id] += 1
    if WARNS[chat_id] < MAX_WARNS:
        await event.reply(WARNING_TEXT)
        return
    else:
        await event.reply(BLOCKING_TEXT)
    full = await event.client(GetFullUserRequest(event.chat_id))
    sender = full.user
    await event.edit(
        f"[{sender.first_name}](tg://user?id={sender.id}) has been blocked."
    )
    await asyncio.sleep(2)
    await event.client(BlockRequest(sender.id))
    text = f"""#Blocked
First name: {sender.first_name}
Last name: {sender.last_name}
Chat id: [{sender.id}](tg://user?id={sender.id})
has been blocked by the PMSecurity."""
    await event.client.send_message(LOGGING_GROUP, text)


@client.on(
    events.NewMessage(pattern="\.av$", outgoing=True, func=lambda e: e.is_private)
)
async def approve_chat(event):
    if event.fwd_from:
        return
    full = await event.client(GetFullUserRequest(event.chat_id))
    chat = full.user
    if api.is_approved(chat.id):
        await event.edit(
            f"[{chat.first_name}](tg://user?id={chat.id}) is already approved in TGPartner PMSecurity system."
        )
    else:
        try:
            api.approve(
                chat.id,
                name=chat.first_name,
                username=chat.username,
            )
            await event.edit(
                f"[{chat.first_name}](tg://user?id={chat.id}) has been successfully approved in TGPartner PMSecurity system."
            )
        except Exception as e:
            await event.edit("Some error occurred")
            print(e)
    await asyncio.sleep(4)
    await event.delete()


@client.on(
    events.NewMessage(pattern="\.dav$", outgoing=True, func=lambda e: e.is_private)
)
async def disapprove_chat(event):
    if event.fwd_from:
        return
    full = await event.client(GetFullUserRequest(event.chat_id))
    chat = full.user
    if not api.is_approved(chat.id):
        await event.edit(
            f"[{chat.first_name}](tg://user?id={chat.id}) is already not approved in TGPartner PMSecurity system."
        )
    else:
        try:
            api.disapprove(chat.id)
            await event.edit(
                f"[{chat.first_name}](tg://user?id={chat.id}) has been successfully disapproved in TGPartner PMSecurity system."
            )
        except Exception as e:
            await event.edit("Some error occurred")
            print(e)
    await asyncio.sleep(4)
    await event.delete()


@client.on(
    events.NewMessage(pattern="\.block$", outgoing=True, func=lambda e: e.is_private)
)
async def block_chat(event):
    if event.fwd_from:
        return
    full = await event.client(GetFullUserRequest(event.chat_id))
    chat = full.user
    if api.is_approved(chat.id):
        api.disapprove(chat.id)
    await event.edit(f"[{chat.first_name}](tg://user?id={chat.id}) has been blocked.")
    await asyncio.sleep(3)
    await event.client(BlockRequest(chat.id))


@client.on(
    events.NewMessage(
        pattern="\.unblock$",
        outgoing=True,
        func=lambda e: e.is_private,
    )
)
async def unblock_user(event):
    if event.fwd_from:
        return
    full = await event.client(GetFullUserRequest(event.chat_id))
    chat = full.user
    await event.edit(f"Unblocking [{chat.first_name}](tg://user?id={chat.id}).")
    await asyncio.sleep(1)
    await event.client(UnblockRequest(chat.id))
    await event.edit(
        f"[{chat.first_name}](tg://user?id={chat.id}) has been unblocked."
    )
