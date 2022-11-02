# Liam-s-Python-Bot

Welcome to my Python Bot!

This simple bot uses python code in order to achieve 3 functions

1. Madlibs

It can run a simple madlibs game, where it will tell you parts of speech to write, and then will output a funny story edited by you!

  Commands:
  - madlibs: starts the madlibs game and prompts user with what to input. Inputs are stored in json file
  - ml: command followed by inputs for madlibs, returns filled in madlibs

2. Rock Paper Scissors

It can play rock paper scissors, and after one person wins 3 rounds it will declare a winner
The bot also has a command to update the user on scores whenever they want

  Commands:
  - rps (r, p, s): command to run the rock paper scissors logic (also includes win conditions), saves outcome in json file
  - RPS Scores: command that displays scores pulled from json file

3. Quizzing

The biggest portion of the bot is its quizzing abilities. 
The bot can add terms to a list similar to quizlet, and then can quiz the user through multiple choice, written answers, and true and false!
This bot can also update the user giving the number correct and percentage correct

  Commands:
  - Display Terms: command that displays all the terms stored in the json file
  - addterm: command that you can write terms and definitions after to add to the json file
  - mc: command that displays a multiple choice question and stores the answer in json
  - (a, b, c, or d): commanda that answer multiple choice question, and information from json determine whether it was correct 
  - wr: command that gives a term for the user to write the definition to and stores the correct answer in json
  - write (answer): command followed by answer to write prompt and determines whether it was right, stores score in json
  - I was right: command that reverses scoring of write in case user has a typo (prevents score spamming with temp-resp variable)
  - tf: command to give the user a true/false question
  - (True/False): answer to true/false question, result stored in json
  - Quizlet Results: gives results of scores pulled from json

Thanks: replies with you are welcome

The bot was developed through the usage of https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ as a preliminary understanding tool.
Then, with the occasional help of Stack Overflow, Mush, and the rest of the ATCCS class the bot became a reality.



**Explanation in Layperson Terms!**

This app connects to Discord in order to send and recieve commands between the code I wrote to Discord itself.
At the start, it loads everything necessary to function, and resets all stored scores, values, etc.
The bot uses a style of commands where it searches each message in the channel for commands:

  - When a person types into the channel, the bot sees that it is a message, and runs through the message through a list of commands.
  - If the name of a command matches the message written in the channel, the bot activates that part of the program.
  - It runs through all of the instructions in that part: Doing whatever it needs to with the input, then outputting a message back to the Discord channel
  - Then, it is ready once again to listen to more commands

For example, my RPS Scores command goes like this:

- I type "RPS Scores" into discord
- The bot recognizes I wrote a message, and sees that it matches the command also named "RPS Scores"
- It takes the scores saved in the program, and sends them as a message to the Discord Channel
- I see the reply and know the current scores of the game!



Explanation in layperson to come!
