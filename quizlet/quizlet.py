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

data['score'] = 0

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
    data['tempDefinitions'] = data['definitions']
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    term_choice = random.randint(0, len(data['terms']))
    
    #term_or_def = random.randint(0, 1)
    
    print(data['tempDefinitions'])
    print(term_choice)
    correct_choice = data['tempDefinitions'][term_choice]
    
    #i have to make it tempDefinitions
    await ctx.channel.send(f"What is the definition of {data['terms'][term_choice]}")
    temp_defs = data['tempDefinitions']
    actual_temp_defs = temp_defs

    answers = []
    answers.append(actual_temp_defs[term_choice])
    actual_temp_defs.remove(data['tempDefinitions'][term_choice])



    random.shuffle(actual_temp_defs)
    answers.append(actual_temp_defs[0])
    answers.append(actual_temp_defs[1])
    answers.append(actual_temp_defs[2])
    random.shuffle(answers)
    


    await ctx.channel.send(f"Is it \n A. {answers[0]} \n B. {answers[1]} \n C. {answers[2]} \n D. {answers[3]} ")
    
    if correct_choice == answers[0]:
        ans = "a"
    elif correct_choice == answers[1]:
        ans = "b"
    elif correct_choice == answers[2]:
        ans = "c"
    else:
        ans = "d"

    data['ans'] = ans
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)



@bot.command()
async def a(ctx):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    if data['ans'] == "a":
        data['score'] += 1
        await ctx.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
    else:
        await ctx.channel.send(f"Incorrect, the correct answer was {data['ans']}")
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)
        
@bot.command()
async def b(ctx):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    if data['ans'] == "b":
        data['score'] += 1
        await ctx.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
    else:
        await ctx.channel.send(f"Incorrect, the correct answer was {data['ans']}")
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)

@bot.command()
async def c(ctx):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    if data['ans'] == "c":
        data['score'] += 1
        await ctx.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
    else:
        await ctx.channel.send(f"Incorrect, the correct answer was {data['ans']}")
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)

@bot.command()
async def d(ctx):
    with open("quizlet/quizlet.json", "r") as f:
        data = json.load(f)
    if data['ans'] == "d":
        data['score'] += 1
        await ctx.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
    else:
        await ctx.channel.send(f"Incorrect, the correct answer was {data['ans']}")
    with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)

    


    
    

    



    




bot.run(TOKEN)
