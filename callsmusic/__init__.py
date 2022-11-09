from pyrogram import Client
from config import SESSION_NAME, API_ID, API_HASH
from .callsmusic import pytgcalls, run
from . import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
run = client.run
