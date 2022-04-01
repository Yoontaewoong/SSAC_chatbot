from chatterbot import ChatBot
chatbot = ChatBot('Brandon',trainer='chatterbot.trainers.ListTrainers')
chatbot.train([
    "Hello",
    "Hi there!",
    "How are you doing",
    "I'm doing great, how about you",
    "That is good to hear",
    "Thank you",
    "You're welcome"
])
chatbot.train([
    "Good bye!",
    "See you soon!"
])