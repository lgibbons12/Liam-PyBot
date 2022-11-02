# Liam-s-Python-Bot

Welcome to my Python Bot!

This simple bot uses python code in order to achieve 3 cool functions

1. Madlibs

It can run a simple madlibs game, where it will tell you parts of speech to write, and then will output a funny story edited by you!

  Commands:
  - madlibs: Starts the madlibs game and prompts user with what to input
  - ml: Command that you write and then followed by inputs for madlibs

2. Rock Paper Scissors

It can play rock paper scissors, and after one person wins 3 rounds it will declare a winner
The bot also has a command to update the user on scores whenever they want

  Commands:
  - rps (r, p, s): Function to run the rock paper scissors logic (also includes win conditions)
  - RPS Scores: displays scores pulled from json file

3. Quizzing

The biggest portion of the bot is its quizzing abilities. 
The bot can add terms to a list similar to quizlet, and then can quiz the user through multiple choice, written answers, and true and false!
This bot can also update the user giving the number correct and percentage correct

  Commands:
  - Display Terms: displays all the terms stored in the json file
  - addterm: command that you can write terms and definitions after to add to the json file
  - mc: command that displays a multiple choice question and stores the answer in json
  - (a, b, c, or d): answers multiple choice question
  - wr: gives a term for the user to write the definition to, stores the correct in json
  - write ~: command followed by answer to write prompt, determines whether it was right
  - I was right: command that reverses scoring of write in case user has a typo (prevents score spamming with temp-resp variable)
  - tf: command to give the user a true/false question
  - (True/False): answer to true/false question
  - Quizlet Results: gives results of scores

Thanks: replies with you are welcome

The bot was developed through the usage of https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ as a preliminary understanding tool.
Then, with the occasional help of Stack Overflow, Mush, and the rest of the ATCCS class the bot became a reality.


This app uses discords api in order to send and recieve commands between the code running in VS Code through PowerShell to Discord itself
Although discord.py does not use slash commands, using client.on_message allows the bot to take in commands based on what users type in the channels

Explanation in layperson to come!
