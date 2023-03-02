import asyncio
import random
import discord
from googletrans import Translator
from src.chatBotFunctions import generate_response

# Initiates the translater
# Please note translator version is 4.0.0 as the current stable version 3.0.0 does not work properly
translator = Translator()

# Reads the file and stores it in a list to be used when the randomFact() function is called
with open('resources/randomfacts', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Reads the file and stores it in a list to be used when the randomQuotes() function is called
with open('resources/quotes', encoding='utf-8') as q:
    quotes = q.readlines()

# Colors I defined, so it's easier to access certain colors when dealing with embeds
colors = {
    'red': 0xff0000,
    'green': 0x00ff00,
    'blue': 0x0000ff,
    'yellow': 0xffff00,
    'orange': 0xffa500,
    'purple': 0x800080,
    'pink': 0xffc0cb,
    'gray': 0x808080,
    'white': 0xffffff,
    'black': 0x000000
}

# Randomly chooses a word from this to keep the embed title interesting
factDescription = ['Thrilling', 'Exhilarating', 'Stimulating', 'Electrifying', 'Rousing', 'Arousing', 'Captivating',
                   'Engaging', 'Enthralling', 'Enchanting', 'Fascinating', 'Mesmerizing', 'Gripping', 'Compelling',
                   'Riveting']

# Randomly chooses a word from this to keep the embed title interesting
quoteDescription = ['Motivating', 'Encouraging', 'Uplifting', 'Stimulating', 'Galvanizing', 'Enlivening',
                    'Invigorating', 'Emboldening', 'Inspiriting', 'Electrifying', 'Empowering', 'Cheering',
                    'Heartening', 'Refreshing', 'Activating']


def randomFact():
    random_fact = random.choice(lines)
    factDesc = random.choice(factDescription)
    embed = discord.Embed(title="Harumi's " + factDesc + " Fact", description=random_fact,
                          color=colors['blue'])
    return embed


def randomQuote():
    random_quote = random.choice(quotes)
    quoteDesc = random.choice(quoteDescription)
    embed = discord.Embed(title="Harumi's " + quoteDesc + " Quote", description=random_quote,
                          color=colors['yellow'])
    return embed


def helpFunction():
    embed = discord.Embed(title="Harumi Help", description="Hey darling, I'm Harumi",
                          color=colors['black'])
    embed.add_field(name="!help",
                    value="You just used this. I can help you when you use this command",
                    inline=False)
    embed.add_field(name="!work",
                    value="Let's work and make some sweet sweet cash", inline=False)
    embed.add_field(name="!fact",
                    value="You receive a random fact", inline=False)
    embed.add_field(name="!quote",
                    value="You receive a random quote", inline=False)
    embed.add_field(name="!translate",
                    value="I translate the message to English :)", inline=False)
    embed.add_field(name="!poll",
                    value="I create a simple Yes or No poll which lasts for 10 minutes", inline=False)
    embed.add_field(name="!chat",
                    value="One of my highlight features. Type !chat and say something to talk with me.", inline=False)
    embed.set_image(url="https://pbs.twimg.com/profile_images/1498079070227099649/-2NWkrq3_400x400.jpg")
    return embed


async def translateFunction(message):
    if message.reference:
        try:
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            await message.reply(embed=translateToEnglish(replied_message.content))
        except discord.errors.NotFound:
            await message.reply("The replied message could not be found.")
    else:
        await message.reply("Please reply to a message to translate it.")


def translateToEnglish(text):
    translation = translator.translate(text, dest='en')
    embed = discord.Embed(title="Harumi's Translation To English", color=colors['orange'])
    embed.add_field(name="Original Text:",
                    value=text, inline=False)
    embed.add_field(name="Translated Text:",
                    value=translation.text, inline=False)
    return embed


def pollEmbed(text):
    embed = discord.Embed(title="Harumi's Poll", description=text, color=colors['blue'])
    return embed


def pollResults(question, ticks, cross):
    description = '\n' + question + '\n\n**Yes** votes: ' + str(ticks) + '\n**No** votes: ' + str(cross)
    embed = discord.Embed(title="Harumi's Poll Results", description=description, color=colors['orange'])
    return embed


async def chatFunction(message):
    chat_input = message.content.split('!chat ')[1]
    chat_output = generate_response(chat_input)
    await message.reply(chat_output)


async def pollFunction(message):
    poll_question = message.content.split('!poll ')[1]
    poll = await message.reply(embed=pollEmbed(poll_question))
    message = poll
    # Add tick and cross reactions
    await message.add_reaction('✅')
    await message.add_reaction('❌')

    # Wait for 5 minutes
    await asyncio.sleep(300)

    # Get updated message with vote counts
    message = await message.channel.fetch_message(poll.id)

    # Get vote counts
    tick_count = 0
    cross_count = 0
    for reaction in message.reactions:
        if reaction.emoji == '✅':
            tick_count = reaction.count - 1  # Subtract the bot's reaction
        elif reaction.emoji == '❌':
            cross_count = reaction.count - 1  # Subtract the bot's reaction

    # Send poll results
    await message.reply(embed=pollResults(poll_question, tick_count, cross_count))
