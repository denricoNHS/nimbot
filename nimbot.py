import os
import rand

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
    await ctx.send(random.choices(["Heads", "Tails"]))

@bot.command(name="average")
async def average(ctx, a, b):
    await ctx.send( (a+b)/2 )

@bot.command(name="sass")
async def sass(ctx, arg):
    options = ["I didn't ask for your opinion", "*rolls eyes*", "*flips hair and ignores question*", "Shut up, nerd", "Ew", "I'd roast you but I shouldn't burn trash", "There is so much trash coming out of your mouth i can smell it", "Did I ask?", "This is an A B conversation. C your way out of it", "I don't care", "Ugh", "Leave me alone", "Who are you again?", "Woow that's craazy *sarcasm*"]
    num = random.randint(0, 13)
    await options[num]

bot.run(token)



