# COSC310Individual

## Project Description

We are developing a conversational agent named Serenity that talks to the user about their feelings and understands their emotional state, offers information and advice regarding their mental health. The bot can also speak to the user in their preferred language and provide them with external information regarding certain topics of choice.


## How to run the code

1. Import this repository into python IDE of your choice
2. Make sure all necessary packages are installed(nltk, translate, wikipedia, random)
3. Run startbot.py

## Scripts/Classes used

optimizer.py:
InputProcess: this class contains helper methods that are useful in processing input
bot.py
This script contains the methods required to run the bot
startbot.py
This script needs to be run to execute the bot

## New Features

1. Wikipedia API: 
The user can ask the bot to make searches about certain topics and the bot will send the user a summary of it from the associated Wikipedia page. It improves the quality of the chatbot by allowing users to access external information about mental health and disorders, making it a more informative application.

2. Translation API:
The user can ask the bot to speak in a different language. It adds to the bot’s functionality as now it can give output to the user in a language the user is more comfortable with. Though at the moment the user still has to speak English, and the bot will respond in a supported language of their choosing, in future versions the translation functionality can be expanded on to allow users to provide input in their preferred language as well.

