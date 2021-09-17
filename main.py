import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('ODg2Njc4NTU0ODI4NTA1MTY4.YT5FwQ.XmTdflHgIdaaAYWhNPAdMke86bg')