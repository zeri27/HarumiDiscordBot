import random
import discord
from googletrans import Translator

translator = Translator()

with open('resources/randomfacts', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

with open('resources/quotes', encoding='utf-8') as q:
    quotes = q.readlines()

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

factDescription = ['Thrilling', 'Exhilarating', 'Stimulating', 'Electrifying', 'Rousing', 'Arousing', 'Captivating',
                   'Engaging', 'Enthralling', 'Enchanting', 'Fascinating', 'Mesmerizing', 'Gripping', 'Compelling',
                   'Riveting']

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
    embed.set_image(url="https://pbs.twimg.com/profile_images/1498079070227099649/-2NWkrq3_400x400.jpg")
    return embed


def translateToEnglish(text):
    translation = translator.translate(text, dest='en')
    embed = discord.Embed(title="Harumi's Translation To English", color=colors['orange'])
    embed.add_field(name="Original Text:",
                    value=text, inline=False)
    embed.add_field(name="Translated Text:",
                    value=translation.text, inline=False)
    return embed
