import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name="flip_coin")
async def flip_coin():
    await ctx.send(random.choice(["heads","tails"]))
bot.run(token)

import random
@bot.command(name="Baby_Name",help="Write girl and find out girl names and write boy to do the same for boys")
async def baby_names(n):
    girlnames = ("Mia","Dinna","Pam","Anny","Jam","Lena","Karla","Ally","Alex","Kate","Bonnie","Carmen","Emma","Alicia","GG","Ginna","Angie","Jennifer","Ashley","May","Kimberly","Amy","Emily","Halsey","Selena","Demi","Diana","Valerie","Sofia","Robin","July","Lexi")
    boynames = ("Zack","Cody","Mo","Luis","James","Mike","Liam","Lex","Kobe","Willy","Justin","Nick","Adrian","Leo","David","Andy","Luke","Richard","DJ","Steve","Ken","Mat","Asher","Jack","Sebastian","Oliver","Edward","Mick","Chris","Brandon","CJ","Henry")
    if n == 'girl':
        return (random.choice(girlnames))
    else: 
        return (random.choice(boynames))
