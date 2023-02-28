import asyncio

import discord
from discord import Game, Status

import config
from src.botFunctions import helpFunction, randomFact, randomQuote, pollFunction, translateFunction

TOKEN = config.TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)

userCoins = {"Jahy": 1000}


@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="!help ❤"), status=Status.dnd)
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(str(message.author) + ": " + str(message.content))

    if message.author == client.user:
        return
    else:
        # Check if the message starts with '!'. Only check for content then.
        if message.content.startswith('!'):
            msg = message.content.lower()
            # Help Function: Bot responds with embed that provides information on what the bot can do for each
            # command entered
            if msg.__eq__('!help'):
                await message.reply(embed=helpFunction())
            # Fact Function: Bot responds with a random fact
            elif msg.__eq__('!fact'):
                await message.reply(embed=randomFact())
            # Quote Function: Bot responds with a random quote
            elif msg.__eq__('!quote'):
                await message.reply(embed=randomQuote())
            # Translate Function: Bot translates the message that's been replied to and returns output in English
            # Any language -> English (uses Google Translator API)
            elif msg.__eq__('!translate'):
                await translateFunction(message)
            elif msg.startswith('!poll'):
                await pollFunction(message)
            # No proper command detected -> respond with generic supporting message
            else:
                await message.reply("I could not understand the command. \nPlease type ***!help*** to see everything I "
                                    "can do and all the commands I can respond to.")


async def run_bot():
    try:
        await client.start(TOKEN)
    finally:
        await client.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())
