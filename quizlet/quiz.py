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


intents = discord.Intents.all()
intents.message_content = True
intents.reactions = True

client = discord.Client(intents = intents)





#resetting and loading files from JSON
with open("quizlet/quizlet.json", "r") as f:
    data = json.load(f)

data['score'] = 0

with open('quizlet/quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)


#function that can take in arguments and store it in json
@client.event
async def on_message(message):
    if message.content.startswith("addterm"):
        with open("quizlet/quizlet.json", "r") as f:
            data = json.load(f)
        arguments = message.content.split(" ")
        data['terms'].append(arguments[1])
        data['definitions'].append(arguments[2])
        await message.channel.send("New term added!")
        with open('quizlet/quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    elif message.content == "mc":
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
        await message.channel.send(f"What is the definition of {data['terms'][term_choice]}")
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
        


        await message.channel.send(f"Is it \n A. {answers[0]} \n B. {answers[1]} \n C. {answers[2]} \n D. {answers[3]} ")
        
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


    elif message.content == "a":
        with open("quizlet/quizlet.json", "r") as f:
            data = json.load(f)
        if data['ans'] == "a":
            data['score'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
        else:
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")
        with open('quizlet/quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "b":
        with open("quizlet/quizlet.json", "r") as f:
            data = json.load(f)
        if data['ans'] == "b":
            data['score'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
        else:
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")
        with open('quizlet/quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "c":
        with open("quizlet/quizlet.json", "r") as f:
            data = json.load(f)
        if data['ans'] == "c":
            data['score'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
        else:
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")
        with open('quizlet/quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "d":
        with open("quizlet/quizlet.json", "r") as f:
            data = json.load(f)
        if data['ans'] == "d":
            data['score'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['score']}")
        else:
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")
        with open('quizlet/quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    
    

    



    




client.run(TOKEN)
