from telethon import TelegramClient 
from telethon.connection import StringSession


partner = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
