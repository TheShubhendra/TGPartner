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
from git import Repo
import os
from tgpartner.config import (
    REPO_URL,
)


@client.on(events.NewMessage(pattern=".update", outgoing=True))
async def update(event):
    await event.edit("Updating......")
    repo = Repo()
    if "origin" in repo.remotes:
        origin = repo.remote("origin")
    else:
        origin = repo.create_remote("origin", REPO_URL)
    origin.fetch()
    repo.git.reset("--hard", "origin/main")
    await event.edit("Update successful, restarting the bot.")
    os.system("bash start.sh")
