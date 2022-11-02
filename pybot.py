#imports
import discord
import os
import random
from discord.ext import commands
import json

#.env code to get token
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

#setting up api and connection to discord
intents = discord.Intents.all()
intents.message_content = True
intents.reactions = True
client = discord.Client(intents = intents)



#Quizlet Setup
with open("quizlet.json", "r") as f:
    data = json.load(f)

data['quizlet-score'] = 0
data['numans'] = 0
data['temp_resp'] = 20

with open('quizlet.json', 'w') as f:
        json.dump(data, f, indent=2)


#RPS Setup
with open("rps.json", "r") as f:
    data = json.load(f)

data['rps-counter'] = 0
data['pl score'] = 0
data['op score'] = 0

with open('rps.json', 'w') as f:
        json.dump(data, f, indent=2)



@client.event
async def on_message(message):
    #Bot Introduction
    if message.content == "Intro":
        await message.channel.send("Hello! I am Liam's python bot, and I have 3 main functions: Madlibs, Rock Paper Scissors, and Quizzing")
        await message.channel.send("If you would like to learn more about any of the 3, please type their name as you see above")
    
    if message.content == "Madlibs":
        await message.channel.send("For Madlibs, please type madlibs (exactly as you see it here), and you will be given instructions")
        await message.channel.send("Then, type ml with spaces for each of the terms requested!")
    
    if message.content == "Rock Paper Scissors":
        await message.channel.send("For RPS, please type rps followed by a space and then your choice of r, p, or s")
        await message.channel.send("If you would like to be updated about scores, please type Scores")
    
    if message.content == "Quizzing":
        await message.channel.send("I can also be your own quizlet bot! (Because quizlet is dumb and makes you pay now)")
        await message.channel.send("If you type addterm followed by a space, then the term, another space, then the definition, it will add that to the list (i.e. addterm hola hello would be a command to add hola to the term list and hello as its definition)")
        await message.channel.send("For multiple choice, just type mc, and then respond with a, b, c, or d for you answer")
        await message.channel.send("For writing, just type wr to get your prompt, and then write with a space followed with your answer exactly")
        await message.channel.send("For true or false, just type tf to get the prompt, and respond with True or False")
        await message.channel.send("To see how you are doing, just type Results")
    
    
    #Madlibs Commands
    #opening code to prompt user with madlibs
    if message.content == "madlibs":
        with open("madlibs.json", "r") as f:
            config = json.load(f)
        number = config['madlibs-num']
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
        await message.channel.send(f"Welcome to Mad Libs! For this one, please write ml, followed by {enters[0]} and {enters[1]} (seperated by spaces)")
   
    #response code for madlibs
    if message.content.startswith("ml"):
        with open("madlibs.json", "r") as f:
            config = json.load(f)
        number = config['madlibs-num']

        #takes the message and splits up the components of the madlibs
        args = message.content.split(" ")
        arg1 = args[1]
        arg2 = args[2]

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

        
        await message.channel.send(response)

        #resets random number for madlibs and sends it to JSON
        config['madlibs-num'] = random.randint(0, 5)
        with open('madlibs.json', 'w') as f:
            json.dump(config, f, indent=2)
    
    #RPS commands
    if message.content.startswith("rps"):
        args = message.content.split(" ")
        arg = args[1]

        

        #load data from JSON and store it in temporary variables
        with open("rps.json", "r") as f:
            data = json.load(f)
        temp_p_score = data['pl score']
        temp_o_score = data['op score']
        

        #welcome message on first playthrough
        if data['rps-counter'] < 1:
            await message.channel.send("Welcome to Rock, Paper, Scissors! To play please type *rps followed by r, p, or s. First to 3 wins!")
        

        #set opponents choice
        num = random.randint(0, 2)
        if num == 0:
            opChoice = "r"
        elif num == 1:
            opChoice = "p"
        elif num == 2:
            opChoice = "s"
        
        #logic for wins depending on player's choice
        if arg ==  "r" or arg == "p" or arg == "s":
            plChoice = arg
            if opChoice == "r":
                if plChoice == "r":
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "p": 
                    temp_p_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "s": 
                    temp_o_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
            elif opChoice == "p":
                if plChoice == "r":
                    temp_o_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "p": 
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "s": 
                    temp_p_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
            else:
                if plChoice == "r":
                    temp_p_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Win! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "p": 
                    temp_o_score += 1
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"You Lose! Player: {temp_p_score} Opponent: {temp_o_score}")
                elif plChoice == "s": 
                    await message.channel.send("Rock, Paper, Scissors!")
                    await message.channel.send(f"Tie! Player: {temp_p_score} Opponent: {temp_o_score}")
        else:
            await message.channel.send("Sorry, we could not get that, please type rps followed by a lowercase r, p, or s")
        
        #logic for winning rps
        if temp_p_score == 3:
            secret = '**You Won!!!!!! Congratulations!**'
            response = "||{}||".format(secret)
            await message.channel.send(response)
            await message.channel.send("||{}||".format("Resetting All Values Now. . ."))
            data['pl score'] = 0
            data['op score'] = 0
            data['rps-counter'] = 0
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent=2)
        elif temp_o_score == 3:
            secret = '**The opponent won :(**'
            response = "||{}||".format(secret)
            await message.channel.send(response)
            await message.channel.send("||{}||".format("Resetting All Values Now. . ."))
            data['pl score'] = 0
            data['op score'] = 0
            data['rps-counter'] = 0
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent=2)
        else: 
            #writing the results back to the JSON file
            data['pl score'] = temp_p_score 
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent=2)
            data['op score'] = temp_o_score
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent=2)
            data['rps-counter'] += 1
            with open('rps.json', 'w') as f:
                json.dump(data, f, indent=2)

    #displays current scores of rps game
    if message.content == "Scores":
        with open("rps.json", "r") as f:
            data = json.load(f)
        await message.channel.send(f"Player: {data['pl score']} Opponent: {data['op score']}. Games Played: {data['rps-counter']}")
    
        


    #Quizlet Commands
    if message.content.startswith("Display Terms"):
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        num = len(data['terms'])
        for i in range(0, num):
            await message.channel.send(f"Term: {data['terms'][i]}; Definition: {data['definitions'][i]}")
        
    #logic to add term to quizlet json
    elif message.content.startswith("addterm"):
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        

        #splits arguments and adds them to the list
        arguments = message.content.split(" ")
        counter = 2
        if (len(arguments) % 2) == 0:
            await message.channel.send("Please enter a definition for each term")
        else:
            if len(arguments) < 4:
                await message.channel.send("New term added!")
            else:
                await message.channel.send("New terms added!")
            for i in range(1, len(arguments)):
                if (counter % 2) == 0:
                    data['terms'].append(arguments[i])
                else:
                    data['definitions'].append(arguments[i])
                counter += 1

            

            with open('quizlet.json', 'w') as f:
                json.dump(data, f, indent=2)

    #multiple choice prompt
    elif message.content == "mc":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['tempDefinitions'] = data['definitions']
        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        term_choice = random.randint(0, len(data['terms']) - 1)
        
        #selects corrent choice
        correct_choice = data['tempDefinitions'][term_choice]
        
        await message.channel.send(f"What is the definition of {data['terms'][term_choice]}")

        #creates new temporary list to pull out wrong definitions
        actual_temp_defs = data['tempDefinitions']
        answers = []
        answers.append(actual_temp_defs[term_choice])
        actual_temp_defs.remove(data['tempDefinitions'][term_choice])


        #creates list of answers
        random.shuffle(actual_temp_defs)
        answers.append(actual_temp_defs[0])
        answers.append(actual_temp_defs[1])
        answers.append(actual_temp_defs[2])
        random.shuffle(answers)
        


        await message.channel.send(f"Is it \n A. {answers[0]} \n B. {answers[1]} \n C. {answers[2]} \n D. {answers[3]} ")
        
        #logic to determine correct choice
        if correct_choice == answers[0]:
            ans = "a"
        elif correct_choice == answers[1]:
            ans = "b"
        elif correct_choice == answers[2]:
            ans = "c"
        else:
            ans = "d"

        #writes correct choice back to json
        data['ans'] = ans
        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)

    
    elif message.content == "a":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "a":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "b":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "b":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "c":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "c":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)



    elif message.content == "d":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "d":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    #prompt for writing
    elif message.content == "wr":
        with open("quizlet.json", "r") as f:
            data = json.load(f)

        num = random.randint(0, len(data['terms']) - 1)

        await message.channel.send(f"What is the definition of {data['terms'][num]}")

        #saves correct answers to json
        data['ans'] = data['definitions'][num]
        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)

    #answering for writing
    elif message.content.startswith("write"):
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        
        #grabs the answer from the message
        msg_list = message.content.split(" ")
        msg = msg_list[1]

        if msg == data['ans']:
            data['quizlet-score'] += 1
            data['numans'] += 1
            data['temp_resp'] = 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            data['temp_resp'] = 0
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    elif message.content == "I was right":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        if data['temp_resp'] == 0:
            data['quizlet-score'] += 1
            await message.channel.send(f"Sorry, your score has been updated. Current Score: {data['quizlet-score']}")
            data['temp_resp'] = 20
        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        
        
        

    
    #prompt for true or false
    elif message.content == "tf":
        with open("quizlet.json", "r") as f:
            data = json.load(f)

        #takes two random numbers and decides if they are the same or not
        num1 = random.randint(0, len(data['terms']) - 1)
        num2 = random.randint(0, len(data['terms']) - 1)
        if num1 == num2:
            data['ans'] = "True"
        else:
            data['ans'] = "False"

        await message.channel.send(f"The definition of {data['terms'][num1]} is {data['definitions'][num2]} (True or False?)")

        #dumps whether it was true or false back to json
        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    

    elif message.content == "True":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "True":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    

    elif message.content == "False":
        with open("quizlet.json", "r") as f:
            data = json.load(f)
        data['temp_resp'] = 20

        if data['ans'] == "False":
            data['quizlet-score'] += 1
            data['numans'] += 1
            await message.channel.send(f"Correct! You got it right! Your Score: {data['quizlet-score']}")

        else:
            data['numans'] += 1
            await message.channel.send(f"Incorrect, the correct answer was {data['ans']}")

        with open('quizlet.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    #code to display current results of quizzing
    elif message.content == "Results":
        with open("quizlet.json", "r") as f:
            data = json.load(f)

        await message.channel.send(f"You have gotten {data['quizlet-score']} correct out of {data['numans']}")

        #logic for giving percentages
        percent = 100 * (data['quizlet-score'] / data['numans'])
        await message.channel.send(f"{percent}%")
        if percent > 0.8:
            await message.channel.send("You are doing great!")
        else:
            await message.channel.send("Do Better")
    
    elif message.content == "Thanks":
        await message.channel.send("You are welcome :)")


client.run(TOKEN)