import os
import random
import requests
import aiohttp

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim', help="Should play a game of nim")
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")


@bot.command(name='flip_coin', help= "50/50 chance. Heads or tails?")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name="avg", help="Gets the average of multiple numbers")
async def avg(ctx, *args: float):
    await ctx.send(sum(args) / len(args))

@bot.command(name="joke", help="bad dad jokes")

async def joke(ctx):
    async with aiohttp.ClientSession(headers={"Accept":"application/json"}) as session:
        async with session.get("https://icanhazdadjoke.com/") as resp:
            data = await resp.json()
            await ctx.send(data["joke"])

@bot.command(name="d6", help="Rolls a 6-sided die")
async def d6(ctx):
    await ctx.send(random.randint(1, 7))


@bot.command(name="fib", help="Creates a sequence of fibonacci numbers")
async def fibonacci(ctx, n: int):
    fib = []
    if n > 0:
        a, b = 0, 1
        for _ in range(n):
            fibonachos.append(a)
            a, b = b, a + b
    elif n < 0:
        a, b = 0, -1
        for _ in range(abs(n)): # list(range()) does not work with negatives
            fibonachos.append(a)
            a, b = b, a - b
    await ctx.send(fibonachos)

bot.run(token)
