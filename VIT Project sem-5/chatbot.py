import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

english_bot = ChatBot('Bot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'},  
                                ], trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)
english_bot.initialize

while(True):
    userText = input("user : ")
    response = str(english_bot.get_response(userText))
    print("Bot : " + response[2:])
    if(userText == "exit" or userText == "Exit" or userText == "Bye" or userText == "bye"):
        break