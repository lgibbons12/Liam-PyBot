#imports
import discord
import os
import random
from discord.ext import commands
import json
import asyncio

#.env code to get token
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")


#setting up the api for the client side and the bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents, command_prefix="*")


#simple ping pong command
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

#resetting and loading files from JSON
with open("rps/rps.json", "r") as f:
    data = json.load(f)
data['counter'] = 0
data['pl score'] = 0
data['op score'] = 0
with open('rps/rps.json', 'w') as f:
        json.dump(data, f, indent=2)

with open("rps/rps.json", "r") as f:
    data = json.load(f)




#main command for rock paper scissors
@bot.command()
async def rps(ctx, arg):
    #load data from JSON and store it in temporary variables
    with open("rps/rps.json", "r") as f:
        data = json.load(f)
    temp_p_score = data['pl score']
    temp_o_score = data['op score']
    

    #welcome message on first playthrough
    if data['counter'] < 1:
        await ctx.channel.send("Welcome to Rock, Paper, Scissors! To play please type *rps followed by r, p, or s. First to 3 wins!")
    

    #set opponents choice
    num = random.randint(0, 2)
    if num == 0:
        opChoice = "r"
    elif num == 1:
        opChoice = "p"
    elif num == 2:
        opChoice = "s"
    async with ctx.typing():
        await asyncio.sleep(4)
    #logic for wins depending on player's choice
    if arg ==  "r" or arg == "p" or arg == "s":
        plChoice = arg
        if opChoice == "r":
            if plChoice == "r":
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "p": 
                temp_p_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "s": 
                temp_o_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
        elif opChoice == "p":
            if plChoice == "r":
                temp_o_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "p": 
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "s": 
                temp_p_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
        else:
            if plChoice == "r":
                temp_p_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "p": 
                temp_o_score += 1
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif plChoice == "s": 
                await ctx.channel.send("Rock, Paper, Scissors!")
                await ctx.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
    else:
        await ctx.channel.send("Sorry, we could not get that, please type *rps followed by a lowercase r, p, or s")
    
    if temp_p_score == 3:
        secret = '**You Won!!!!!! Congratulations!**'
        response = "||{}||".format(secret)
        await ctx.channel.send(response)
        await ctx.channel.send("||{}||".format("Resetting All Values Now. . ."))
    elif temp_o_score == 3:
        secret = '**The opponent won :(**'
        response = "||{}||".format(secret)
        await ctx.channel.send(response)
        await ctx.channel.send("||{}||".format("Resetting All Values Now. . ."))
    else: 
        #writing the results back to the JSON file
        data['pl score'] = temp_p_score 
        with open('rps/rps.json', 'w') as f:
            json.dump(data, f, indent=2)
        data['op score'] = temp_o_score
        with open('rps/rps.json', 'w') as f:
            json.dump(data, f, indent=2)
        data['counter'] += 1
        with open('rps/rps.json', 'w') as f:
            json.dump(data, f, indent=2)


#simple command to display current standings
@bot.command()
async def scores(ctx):
    with open("rps/rps.json", "r") as f:
        data = json.load(f)
    await ctx.channel.send(f"Player: {data['pl score']} Opponent: {data['op score']}. Games Played: {data['counter']}")
    




bot.run(TOKEN)
