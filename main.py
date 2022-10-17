import discord
import os
import requests
import json
from discord.ext import commands


from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")


mad_lib_bool = False
def mad_libs(w1, w2):
    global response
    response = f"It was a bright morning and Jim was wearing his {w1} pants. After a nice {w2}, he went to work"
    return response

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents, command_prefix="$")


@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def mad_libs(ctx):
    mad_lib_bool = True
    await ctx.channel.send("Welcome to Mad Libs! For this one, please write $args, followed by an adjective and a verb")
@bot.command()
async def args(ctx, arg1, arg2):
    #mad_libs(arg1, arg2)
    response = f"It was a bright morning and Jim was wearing his {arg1} pants. After a nice {arg2}, he went to work"
    await ctx.send(response)
    

bot.run(TOKEN)

