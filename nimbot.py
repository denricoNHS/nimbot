import os
import random

from discord.ext import commands
from dotenv import load_dotenv

def fibonacci(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    a, b = 0, 1
    for _ in range(n):
        yield sign * a
        a, b = b, a + b

def get_joke():
    url = "https://icanhazdadjoke.com/"
    header = {"Accept" : "application/json"}
    joke = requests.get(url, headers = header).json()
    return joke["joke"]

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='help')
async def help(ctx):
    await ctx.send('''Commands: nim, flip_coin, avg, joke
    nim plays a game of nim,
    flip_coin chooses which side of a coin you get,
    avg gets the average of any amount of numbers,
    joke spits out a bad dad joke please DO NOT SPAM.
    fib gives you a sequence of fibonacci numbers
    ''')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name='flip_coin')
async def flip_coin(ctx):
    await ctx.send(random.choice("Heads", "Tails"))

@bot.command(name='avg')
async def average(ctx, *args: float):
    await ctx.send(sum(*args) / len(*args))

@bot.command(name='joke')
async def tell_joke(ctx):
    await ctx.send(get_joke())

@bot.command(name='fib')
async def fib(ctx, a: int):
    await ctx.send(str(list(fibonacci(a))))

bot.run(token)

