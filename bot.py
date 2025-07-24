# 📁 File: bot.py

import os
import requests
from datetime import datetime
import pytz
import discord

# 🔐 Load secrets from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
THREAD_ID = int(os.getenv("THREAD_ID", 0))
ROLE_ID = os.getenv("ROLE_ID", "")

# 🧠 Set up basic bot client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# 💡 Get quote from ZenQuotes API
def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        if res.status_code == 200:
            data = res.json()[0]
            return f"\u2728 *{data['q']}* — {data['a']}"
    except:
        pass
    return "\ud83d\udca1 Stay focused and do your best!"

# ✅ When bot is ready
@client.event
async def on_ready():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    if now.weekday() < 5:  # 0 = Monday, ..., 4 = Friday
        try:
            channel = await client.fetch_channel(THREAD_ID)
            message = f"<@&{ROLE_ID}> \ud83d\uddce\ufe0f Daily Standup Reminder!\n{get_quote()}"
            await channel.send(message)
        except Exception as e:
            print(f"Error sending message: {e}")
    await client.close()

# 🚀 Start the bot
client.run(TOKEN)
