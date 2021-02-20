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
    upstream.fetch()
    repo.git.reset("--hard", "origin/main")
    await event.edit("Update successful, restarting the bot.")
    os.system("python3 -m tgpartner")
