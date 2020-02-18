import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name=)

@bot.command(name="flip_coin")
async def flip_coin():
    await ctx.send(random.choice(["Heads","Tails"]))


bot.run(token)

#Your name: Anny


