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
    if "upstream" in repo.remotes:
        upstream = repo.remote("upstream")
    else:
        upstream = repo.create_remote("upstream, REPO_URL")
    upstream.fetch()
    repo.git.reset("--hard", "upstream/main")
    await event.edit("Update successful, restarting the bot.")
    os.system("python3 -m tgpartner")