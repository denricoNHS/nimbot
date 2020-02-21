import os
import random
import datetime

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
    await ctx.send(random.choice(["Head", "Tail"]))


@bot.command(name='average')
async def average(ctx, *args: float):
    await ctx.send((sum(args))/len(args)) 

@bot.command(name='date') 
async def date(ctx):
    current = datetime.datetime.now()  
    await ctx.send(("Today is",current.strftime("%A, %B %d, %Y."), "The time is",current.strftime("%I:%M:%S")))

bot.run(token)

