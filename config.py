import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "24869695"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "5ee98927939d175ca953297fbe309f37")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8348059379:AAHiMr-8nMkxwPSthfi5IkowINW-Mwu5lco")

OWNER_ID = int(os.environ.get("OWNER_ID", "7445620075"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7445620075").split("7780806801")))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://editingtution99:kLKimOFEX1MN1v0G@cluster0.fxbujjd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002702049353"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
