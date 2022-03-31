from email import message
from http.client import HTTPResponse
from django.shortcuts import render


# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# Create your views here.
def index(request):
    return render(request, 'chatbot/main.html')

def post(self, request):
    # POST 된 Form 데이터 얻기
        form = ImageForm(req.POST, req.FILES)
        # Form data 에러 체크
        if not form.is_valid():
            raise ValueError('invalid form')
        # Form data로 부터 이미지 파일 얻기
        image = form.cleaned_data['image']
        # 이미지 파일을 지정하여 얼굴 분류
        result = detect(image)
        # 얼굴 분류의 결과 저장
        self.params['result_list'], self.params['result_name'], self.params['result_img'] = result
        # 페이지에 화면 표시
        return render(req, 'pred/index.html', self.params)
# Create a new instance of a ChatBot
# bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

# trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.english")

# def index(request):
# 	if request.method == "POST":
# 		print("yha aaya")
# 		message = request.POST["message"]
# 		message=message.lower()
# 		print(message)
# 		if message=="bye":
# 			bot_response=ending()
# 		elif message=="what is your name" or message=="who are you":
# 		    bot_response="My name is MyBot. I am a Robo."
# 		else:
# 			if(message[:4]=='what' or message[:3]=='who'):
# 				# if(wiki(message)==False):
# 					bot_response="Sorry, I didn't get it."
# 					print("Sorry, I didn't get it.")
# 				#else:
# 				#    bot_response=wiki(message)
# 		# 	else:
# 		# 	    bot_response = str(bot.get_response(message))
# 		# return HTTPResponse(bot_response)
# 	else:
# 		bot_response=""
# 		# response=greeting()
# 		# print(response)
# 		return render(request,"chatbot/main.html")




