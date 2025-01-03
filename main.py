import discord 
import asyncio
token = "token here" 
client = discord.Client() 
@client.event 
async def on_ready(): 
    print(f'Logged in as {client.user}') 
    await client.change_presence(activity=discord.Game(name=" uptime")) 
@client.event 
async def on_message(message): 
    if message.content.startswith('!hi'): 
        await message.channel.send('# hiiii) 
client.run(token, bot=False) 
