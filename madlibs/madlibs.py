import discord
import os
import random
from discord.ext import commands
import json

with open("madlibs/madlibs.json", "r") as f:
    config = json.load(f)

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

global number
number = config['num']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents, command_prefix="/")


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command()
async def madlibs(ctx):
    global enters
    enters = []
    if number == 0:
        enters = ["adjective", "active verb"]
    elif number == 1:
        enters = ["verb that ends in -ing", "adjective"]
    elif number == 2:
        enters = ["color", "shape"]
    elif number == 3:
        enters = ["plural noun", "adverb"]
    elif number == 4:
        enters = ["number", "proper noun"]
    else:
        enters = ["videogame", "adjective"]
    
    
    await ctx.channel.send(f"Welcome to Mad Libs! For this one, please write $args, followed by {enters[0]} and {enters[1]}")
@bot.command()
async def args(ctx, arg1, arg2):
    global number
    response = ""
    if number == 0:
        response = f"John was on his way to the market when a {arg1} person approached him and {arg2}."
    elif number == 1:
        response = f"I was {arg1} when all of a sudden my {arg2} friend stabbed me in the back."
    elif number == 2:
        response = f"I am a famous painter. When I painted my first {arg1} masterpiece, some said it looked like a {arg2}, however I knew it looked like a banana."
    elif number == 3:
        response = f"There were {arg1} everywhere as the kids {arg2} sprinted around the room"
    elif number == 4:
        response = f"There were {arg1} people standing around {arg2} when everything went to shambles."
    else:
        response = f"I was busy playing {arg1} when all of a sudden a {arg2} attacked me."

    config['num'] = random.randint(0, 5)
    number = config['num']
    await ctx.channel.send(response)
    


bot.run(TOKEN)

