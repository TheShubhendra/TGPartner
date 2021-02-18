from telethon.sync import events


@client.on(events.NewMessage)
async def test(event):
    if event.text == "ping":
        await event.edit("pong")
