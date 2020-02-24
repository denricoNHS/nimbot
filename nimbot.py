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

@bot.command(name= 'average')
async def average(ctx, a, b):
    await ctx.send(a+b/2)
    
@bot.command(name= 'quotes')
async def quotes(ctx):
    await ctx.send(random.choice(["Genius is one percent inspiration and ninety-nine percent perspiration.","You can observe a lot just by watching.","A house divided against itself cannot stand.","Difficulties increase the nearer we get to the goal.", "Fate is in your hands and no one elses","Be the chief but never the lord.","Nothing happens unless first we dream.","Well begun is half done.","Life is a learning experience, only if you learn.","Self-complacency is fatal to progress.","Peace comes from within. Do not seek it without.","What you give is what you get.","We can only learn to love by loving.","Life is change. Growth is optional. Choose wisely."]))
bot.run(token)
#Tatiana Nunez

