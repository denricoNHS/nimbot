import os
import random 

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name='flip_coin')
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

bot.run(token)


@bot.commad(name='average')
async def average(ctx, a, b):
    await ctx.send[(a + b)/2]


@bot.commad(name="even_or_odd")
async def even_or_odd(ctx, number):
    if number % 2 == 0:
        await ctx.send("Even")
    else:
        await ctx.send("Odd")

#vicky 



