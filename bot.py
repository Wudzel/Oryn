import discord
import os
import sys

token = os.environ["DISCORD_TOKEN"]
channel_id = int(os.environ["DISCORD_CHANNEL_ID"])

# Split the single string of files into a list
files_to_send = sys.argv[1].split() if len(sys.argv) > 1 else []

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = await client.fetch_channel(channel_id)
    if not files_to_send:
        print("No files to send")
        await client.close()
        return
    for filepath in files_to_send:
        if os.path.exists(filepath):
            await channel.send(file=discord.File(filepath))
            print(f"Sent: {filepath}")
        else:
            print(f"File not found: {filepath}")
    await client.close()

client.run(token)
