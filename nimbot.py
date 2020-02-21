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

@bot.command(name="flip-coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name= 'average')
async def average(ctx, *args: float):
    await ctx.send(sum(args)/len(args))

@bot.command(name= 'help')
async def help(ctx):
    await ctx.send(random.choice(["Nah I think you git this 😉", "Help yourself 😠", "I would rather not 😒 " , "YOU ALWAYS ASK FOR HELP BUT NO ONE EVER ASKS ME IF I NEED HELP 😭" ]))


bot.run(token)

#Amy Azogue


