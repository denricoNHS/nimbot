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

@bot.command(name="flip_coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name="average")
async def average(ctx, a, b):
    await ctx.send((a+b)/2)

@bot.command(name="Odds")
async def odds(ctx):
    await random.randint(1,10)

@bot.command(name="d")
async  def alpha(str):
    str_1 = ("Hi, my name is Rosco! Stop doing what I do!")
    words = str_1.split()
    words.sort()
    print("they are in alpha order!")
    for word in words:
        print(word)


bot.run(token)

print("SALSA WAS HERE")
#iwanttogotomecasa








