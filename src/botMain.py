import asyncio

import discord
import datetime
from discord.ext import commands
from discord.ext.commands import CooldownMapping, BucketType
from discord import Game, Status

import config
from src.botFunctions import helpFunction, randomFact, randomQuote, pollFunction, translateFunction

TOKEN = config.TOKEN

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='!')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="!help ❤"), status=Status.dnd)
    print('Logged in as {0.user}'.format(client))


cooldowns = CooldownMapping.from_cooldown(1, 600, BucketType.user)


@client.command()
async def work(ctx):
    if cooldowns.get_bucket(ctx.message).update_rate_limit():
        retry_after = cooldowns.get_bucket(ctx.message).get_retry_after()
        string_time = str(datetime.timedelta(seconds=retry_after)).split(":")
        minutes = int(string_time[1])
        seconds = int(string_time[2].split(".")[0])
        if minutes < 10:
            if minutes > 1:
                await ctx.reply("You are currently on cooldown. Try again in " + str(minutes) + " minutes.")
            else:
                await ctx.reply("Your cooldown is almost over. Try again soon in about " + str(seconds) + " seconds.")
    else:
        # Perform work functionality
        await ctx.reply("You have worked and earned some money!")


@client.command()
async def help(ctx):
    await ctx.reply(embed=helpFunction())


@client.command()
async def fact(ctx):
    await ctx.reply(embed=randomFact())


@client.command()
async def quote(ctx):
    await ctx.reply(embed=randomQuote())


@client.command()
async def translate(ctx):
    await translateFunction(ctx.message)


@client.command()
async def poll(ctx):
    await pollFunction(ctx.message)


async def run_bot():
    try:
        await client.start(TOKEN)
    finally:
        await client.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())
