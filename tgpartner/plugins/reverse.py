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

WORD_REVERSE_ACTIVATED = False
SEN_REVERSE_ACTIVATED = False


@client.on(events.NewMessage(outgoing=True))
async def test(event):
    text = event.text
    if SEN_REVERSE_ACTIVATED:
        sen = text.split()[::-1]
        await event.edit(" ".join(sen))
    elif WORD_REVERSE_ACTIVATED:
        words = text.split()
        words = list(map(lambda x:x[::-1],words))
        await event.edit(" ".join(words))

@client.on(events.NewMessage(pattern=r".reverse (sen|word) (on|off)", outgoing=True))
async def toggle_reverse(event):
    global WORD_REVERSE_ACTIVATED
    global SEN_REVERSE_ACTIVATED
    reverse_type = event.pattern_match.group(1)
    command = event.pattern_match.group(2)
    if reverse_type == "word":
        if command == "on":
            WORD_REVERSE_ACTIVATED = True
            await event.edit("`Word reverse activated.`")
        else:
            WORD_REVERSE_ACTIVATED = False
            await event.edit("`Word reverse deactivated.`")
    elif reverse_type == "sen":
        if command == "on":
            SEN_REVERSE_ACTIVATED = True
            await event.edit("`Sentence reverse activated.`")
        else:
            SEN_REVERSE_ACTIVATED = False
            await event.edit("`Sentence reverse deactivated.`")


@client.on(events.NewMessage(pattern=r".reverse$", outgoing=True))
async def reverse_status(event):
    if WORD_REVERSE_ACTIVATED:
        w = "Activated"
    if not WORD_REVERSE_ACTIVATED:
        w = "Deactivated"
    if SEN_REVERSE_ACTIVATED:
        s = "Activated"
    else:
        s = "Deactivated"
    await event.edit("`Status of reverse plugin\nReverse Word: {}\nReverse Sentence: {}`".format(w,s))