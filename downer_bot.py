# downer_bot.py

import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
counter = 0

with open('positivity.txt') as file:
    posi = file.read().splitlines()

with open('negativityt.txt') as file:
    nega = file.read().splitlines()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '<' in message.content and 'kys' in message.content.lower():
        await message.channel.send(file=discord.File('uno.gif'))

    for word in posi:
        if word in message.content.lower():
            global counter
            counter += 1
            print(f'{counter} positivities detected.')
            if counter > 20:
                path = random.choice(os.listdir('negativity/'))
                counter = random.randint(0, 5)
                coinf = random.randint(0, 5)
                if coinf >= 4:
                    await message.channel.send(file=discord.File('negativity/' + path))
                else:
                    await message.channel.send(random.choice(nega))

client.run(TOKEN)