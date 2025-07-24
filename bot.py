import os
import requests
from datetime import datetime
import pytz
import discord
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("DISCORD_TOKEN")
THREAD_ID = int(os.getenv("THREAD_ID", 0))
ROLE_ID = os.getenv("ROLE_ID", "")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        if res.status_code == 200:
            data = res.json()[0]
            return f"\u2728 *{data['q']}* — {data['a']}"
    except Exception as e:
        logging.error(f"Error fetching quote: {e}")
    return "\ud83d\udca1 Stay focused and do your best!"

@client.event
async def on_ready():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    if now.weekday() < 5:
        try:
            channel = await client.fetch_channel(THREAD_ID)
            message = f"<@&{ROLE_ID}> \ud83d\uddce\ufe0f Daily Standup Reminder!\n{get_quote()}"
            await channel.send(message)
            logging.info("Reminder sent successfully.")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
    await client.close()

client.run(TOKEN)
