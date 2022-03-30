from django.shortcuts import render,redirect
from django.http import HttpResponse
import pyttsx3
import datetime
import wikipedia
import webbrowser

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		bot_response="Good Morning. "
	elif hour>=12 and hour<18:
		bot_response="Good Afternoon. "
	else:
		bot_response="Good Evening. "
	bot_response+="I am MyBot. How can I help you?"
	return bot_response

def ending():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<3 or hour>=20 and hour<=23:
		print("Byee see you tomorrow. Good Night")
		bot_response="Byee see you tomorrow. Good Night"
	else:
		print("Bye. Have a good day")
		bot_response="Bye. Have a good day"
	return bot_response

def wiki(query):
	try:
		query = query.replace("wikipedia","")
		results = wikipedia.summary(query,sentences=2)
		print(*results)
		return results
	except:
		return False


# Create a new instance of a ChatBot
bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

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
				if(wiki(message)==False):
					bot_response="Sorry, I didn't get it."
					print("Sorry, I didn't get it.")
				else:
				    bot_response=wiki(message)
			else:
			    bot_response = str(bot.get_response(message))
		return HttpResponse(bot_response)
	else:
		bot_response=""
		response=greeting()
		print(response)
		return render(request,"index.html",{"response_greeting":response})


