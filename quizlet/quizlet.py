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
with open("quizlet/quizlet.json", "r") as f:
    data = json.load(f)

with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)


#function that can take in arguments and store it in json
@bot.command()
async def addterm(ctx, arg1, arg2):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    data['terms'].append(arg1)
    data['definitions'].append(arg2)
    await ctx.channel.send("New term added!")
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)

@bot.command()
async def multchoice(ctx):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    term_choice = random.randint(0, len(data['terms']))
    #term_or_def = random.randint(0, 1)

    #i have to make it definitions
    await ctx.channel.send(f"What is the definition of {data['terms'][term_choice]}")
    temp_terms = data['terms']
    temp_terms.remove(data['terms'][term_choice])
    print(temp_terms)
    answers = []
    answers.append(data['terms'][term_choice])

    random.shuffle(temp_terms)
    answers.append(temp_terms[0])
    answers.append(temp_terms[1])
    answers.append(temp_terms[2])
    random.shuffle(answers)
    print(answers)
    await ctx.channel.send(f"Is it \n A. {answers[0]} \n B. {answers[1]} \n C. {answers[2]} \n D. {answers[3]} ")
    for i in range(1, 4):
        if data['terms'][term_choice] == answers[i]:
            ans = i
        else:
            pass
    data['ans'] = ans
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)



            

    


    
    

    



    




bot.run(TOKEN)
