import discord
import asyncio
import random

client = discord.Client()

keywords = ["react"]
is_running = False

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    global is_running

    if message.author == client.user:
        return

    if message.content.lower() == '!react':
        async for msg in message.channel.history(limit=10):
            if any(keyword in msg.content.lower() for keyword in keywords):
                try:
                    await asyncio.sleep(2.5)
                    reaction = random.choice(['😂', '✅'])
                    await msg.add_reaction(reaction)
                except discord.Forbidden:
                    print("Nu am permisiunea de a adăuga reacții.")

    elif message.content.lower() == '!start':
        is_running = True
        await message.delete()
        try:
            with open("notepad.txt", "r") as file:
                lines = file.readlines()
            while is_running:
                for line in lines:
                    await message.channel.send(line.strip())
                    await asyncio.sleep(2.5)
        except FileNotFoundError:
            print("Fișierul notepad.txt nu a fost găsit.")

    elif message.content.lower() == '!stop':
        is_running = False
        await message.delete()

client.run('token here')
