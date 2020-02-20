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
    await ctx.send(random.choice(['Heads', 'Tails']))

@bot.command(name='average')
async def average(ctx, *args:float): #this is not working... maybe
    await ctx.send(sum(args)/len(args) )

@bot.command(name= 'FORTUNE_COOKIE')
async def FORTUNE_COOKIE(ctx):
    await ctx.send(random.choice(['your lucky numbers today: 10, 25, 3, 7', 'your lucky numbers today: 3, 4, 6, 7', 'a heart is an upside down butt', 'patience is key', 'the unlit candle scares no monckeys','you will buy new pants on tuesday','because you demand more from yourself, others respect you deeply', 'be careful or you could fall for some tricks today', 'go take a rest, you deserve it', 'if you continually give, you will continually have', 'it takes courage to admit fault', 'the end of something marks the start of something new', 'practice makes perfect... scratch that, practice makes better']))

#I like that... so I'm gonna keep it

bot.run(token)
