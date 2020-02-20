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
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name='avg')
async def avg(ctx,*args: float):
      await ctx.send(sum(args) / len(args))

@bot.command(name='date')
async def count(ctx, datetime):
    await ctx.send(datetime.datetime(2020, 02, 20).strftime('%A'))

    
bot.run(token)