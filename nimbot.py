import os
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv

def get_joke():
    url = "https://icanhazdadjoke.com/"
    header = {"Accept" : "application/json"}
    joke = requests.get(url, headers = header).json()
    return joke["joke"]


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name='flip_coin')
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name="avg")
async def avg(ctx, *args: float):
    await ctx.send(sum(args) / len(args))

@bot.command(name="joke")
async def tell_joke(ctx):
    await ctx.send(get_joke())

bot.run(token)
