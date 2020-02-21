import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command (name =  "years_since_2020")
async def years_since_2020(year):
    await ctx.send(
    a = str(2020 - year)
    b = " years, " 
    c = "which is " + str(int(a)*365) 
    d = " days"
    await(a + b + c + d)) 

bot.run(token)


