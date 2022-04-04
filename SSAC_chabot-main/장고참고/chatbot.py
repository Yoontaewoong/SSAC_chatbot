import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level=logging.CRITICAL)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		print("Good Morning")
		speak("Good Morning")
	elif hour>=12 and hour<18:
		print("Good Afternoon")
		speak("Good Afternoon")
	else:
		print("Good Evening")
		speak("Good Evening")
	print("I am MyBot. How can I help you?")
	speak("I am MyBot. How can I help you?")

def ending():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<3 or hour>=20 and hour<=23:
		print("Byee see you tomorrow. Good Night")
		speak("Byee see you tomorrow. Good Night")
	else:
		print("Bye. Have a good day")
		speak("Bye. Have a good day")

def wiki(query):
	try:
		query = query.replace("wikipedia","")
		results = wikipedia.summary(query,sentences=2)
		speak("Searching...")
		speak("According to wikipedia")
		print(*results)
		speak(results)
		return True
	except:
		return False


# Create a new instance of a ChatBot
bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

greeting()
user_input = input()
while user_input:
	if user_input=="bye":
		ending()
		break
	bot_response = str(bot.get_response(user_input))
	if(bot_response=='How are you?'):
		if(wiki(user_input)==False):
			print("Sorry I didn't get it.")
			speak("Sorry I didn't get it.")
	else:
		print(bot_response)
		speak(bot_response)
	user_input = input()

