import discord
import os
import sys

token = os.environ["DISCORD_TOKEN"]
channel_id = int(os.environ["DISCORD_CHANNEL_ID"])
files_to_send = sys.argv[1:]  # files passed in as arguments

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    for filepath in files_to_send:
        if os.path.exists(filepath):
            await channel.send(file=discord.File(filepath))
            print(f"Sent: {filepath}")
    await client.close()

client.run(token)
