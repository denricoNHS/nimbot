import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name="nim")
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name="flip_coin")
async def flip_coin():
    await ctx.send(random.choice(["Heads","Tails"]))

@bot.command(name= 'average')
async def average(ctx, a: float, b: float):
    await ctx.send[(a + b)/2]

@bot.command(name= 'snapple_facts')
async def snapple_facts():
        await ctx.send(random.choice(["Peaches are members of the almond family.",
        "The Hawaiin alphabet has only 12 letters.","Fish cough!",
        "1/4 of the bones in your body are in your feet.","A tune that gets stuck in your head is called an earworm.",
        "Borborygmi is the noise that your stomach makes when you are hungry.",'The dot over the letter i is called a tittle.',
        "If there are two full moons the second one is called a blue moon.","The infinity is called a lemniscate.",
        "The term rookies comes from a Civil War term, reckie, which was short for recruit.","Chicago is named after smelly grlic that one grew in the area.",
        "Baby bunnies are called kittens.","The word 'bride' comes from an old Proto-Germanic word meaning to 'to cook'.",
        "The word 'checkmate' comes from the Persian phrase meaning 'the kind is dead'.","Cherophobia is the fear of happiness.",
        "Pteronophobia is the fear of being tickled by feathers.","A flock of crows is known as a murder.","Animals that lay eggs don't have a belly button.",
        "The Mona Lisa has no eyelids.","Oysters can change from one gender to another and back again.","No piece of paper can be folded more than seven times.",
        "Googol is a number (1 followed 100 zeros).","Lizards communicate by doing push-ups.","Squids can have eyes the size of a volleyball.",
        "A one-minute kiss burns about 26 calories.","Smelling apples and/or bananas can help you lose weight.","Frogs never drink.",
        "Beavers were once the size of bears.","Seals sleep one and a half minutes at a time.",
        "Pigeons have been trained by the U.S. Cross Guard to spot people lost at sea.","A pigeon's feathers are heavier than its bones.",
        "Penguins have an organ above their eyes that converts seawater to fresh water.","One brow wrinkle is the result of of 200,000 frowns.",
        "The first vacuum was so large, it was brought to a house by horses.",
        "'Q' is the only letter in the alphabet not apppearing in the name of any U.S. state.","Hawaii is the only state with one school distict.",
        "Cows give more milk when they listen to music.","An ostrich's brain is smaller than its eye.",
        "If you doubled one penny everyday for 30 days, you would have $5,368,709.","Colors like red, yellow, and orange make yoou hungry."]))





bot.run(token)

#Your name: Anny


