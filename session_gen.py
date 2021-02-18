from telethon.sync import TelegramClient
from telethon.sessions import StringSession

APP_ID = input("Please Enter your APP_ID: ")
API_HASH = input("Please Enter your API_HASH: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    string = client.session.save()
    print("Your session string is:")
    print(string)
    print()
    print("You can found this on your saved messages too.")
    client.send_message("me", f"`{string}`")
