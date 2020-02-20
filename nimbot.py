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
async def flip_coin():
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name= 'average')
async def average(ctx, a, b):
    await ctx.send(a+b/2)
    
@bot.command(name= 'inspirational_quotes')
async def inspirational_quotes():
    await ctx.send(random.choice(["Your limitation—it's only your imagination.", "Push yourself, because no one else is going to do it for you."]))

bot.run(token)
#Tatiana Nunez

