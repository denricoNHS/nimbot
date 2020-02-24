import os
import random
import requests

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
    await ctx.send(random.choice(["Heads","Tails"]))

@bot.command(name='headline')
async def headline(ctx):
    url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=94b0fd11ba4d4922ae3a3a90b9370872')
    response = requests.get(url)
    await ctx.send(response.json())

bot.run(token)


