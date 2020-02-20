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


@bot.command(name='Enricos_compliments')
async def Enricos_compliments(ctx):           
    await ctx.send(random.choice(["You need to do your eyebrows", "You know you suck right?","My hair is better than yours, and I am bald","You smell like hot Canadian Garbage","I have been to your house and I have concluded that you are fat.","Try not to create something that we have done millions and billions of times before please."]))

bot.run(token)

