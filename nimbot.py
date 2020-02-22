import os
import random
import requests
import aiohttp

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


@bot.command(name="avg")
async def avg(ctx, *args: float):
    await ctx.send(sum(args) / len(args))


@bot.command(name="joke")
async def joke(ctx):
    async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
        async with session.get("https://icanhazdadjoke.com/") as resp:
            data = await resp.json()
            await ctx.send(data["joke"])


@bot.command(name="game")
async def info(ctx, *args: str):
    client_id = "4SJkTSHGOB"
    game = " ".join(args)
    url = f"https://www.boardgameatlas.com/api/search?name={game}&client_id={client_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            cont = await resp.json()
            await ctx.send(cont["games"][0]["description"])

bot.run(token)
