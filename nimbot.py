import os
import datetime

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def casino(ctx):
    print ("1.Coin Flip")
    print ("2.ROll the Dice")
    await("Enter which number game would you like to play")

bot.run('Njg5NTIxNjAyNjgxMjQxNjAz.XnEjgw.-WPeI1GHJcsLc-9mfkTuTmuysJA')

 
 
