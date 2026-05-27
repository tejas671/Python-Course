# import datetime
# import time

# name = input("Swagat hai Enter ypur name : ")
# presenttime =datetime.datetime.now().hour
# if 5 <= presenttime <= 11:
#     print("Good Morning ", name)
# elif 11 < presenttime <= 18:
#     print("Good afternoon ", name)
# else:
#     print("Good Night", name)

import time
# AI Assistant
print("Namaste! Welcome to your Buddy ChatBot")
print("You can ask me basic question and type 'Bye' to Exit from the bot")

#chatbot memory creation dictionaries of responses

responses = {
    "hello" : "hi Welcome how can i help you?",
    "how are you" : "i am very fine",
    "who are you" : " i am smart ai chatbot",
    "motivate me" : "keep going every bug of your projevt makes you a better developer",
    "happy" : "great to hear that",
    "what are functions" : "go and learn chapter 7"
}
def getResponseofbot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "i dont know, i am learning it"

while True:    
#take user input

    userInput = input("Please ask your question : ")
    if "bye" in userInput.lower():
        break
    time.sleep(1)
    reply = getResponseofbot(userInput)
    time.sleep(1)
    print("bot response : ", reply)

    