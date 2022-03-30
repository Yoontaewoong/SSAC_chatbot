from http.client import HTTPResponse
from django.shortcuts import render


# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# Create your views here.
# def index(request):
#     return render(request, 'chatbot/main.html')

# Create a new instance of a ChatBot
# bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

# trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.english")

def index(request):
	if request.method == "POST":
		print("yha aaya")
		message = request.POST["message"]
		message=message.lower()
		print(message)
		if message=="bye":
			bot_response=ending()
		elif message=="what is your name" or message=="who are you":
		    bot_response="My name is MyBot. I am a Robo."
		else:
			if(message[:4]=='what' or message[:3]=='who'):
				# if(wiki(message)==False):
					bot_response="Sorry, I didn't get it."
					print("Sorry, I didn't get it.")
				#else:
				#    bot_response=wiki(message)
		# 	else:
		# 	    bot_response = str(bot.get_response(message))
		# return HTTPResponse(bot_response)
	else:
		bot_response=""
		# response=greeting()
		# print(response)
		return render(request,"chatbot/main.html")




