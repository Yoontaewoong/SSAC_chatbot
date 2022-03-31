from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

import chatbot_model.model_test as test
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
	print("============= index 실행 ==================")
	if request.method == "POST":
		message = request.POST["message"]
		message=message.lower()
		print(message)
		response = test.run(message)
		print(f"대답은 :{response}")
		return HttpResponse(response)

	else:
		bot_response=""
		response="문의 내용을 적어주세요."
		print(response)
		return render(request,"chatbot/main.html",{"response_greeting":response})




