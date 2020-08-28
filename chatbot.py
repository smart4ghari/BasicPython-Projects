#import the necessary libraries
from nltk.chat.util import Chat,reflections

#Predefined set of insturctions
instructions = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me as personal chatbot, else give me some better name ?",]
    ],
    [
        r"your name is (.*)",
        ["Wow %1 is a very good name,Thank you",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],

    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],

    [
        r"i'm doing great thanks for asking",
        ["Happy to hear that",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

#Defining the function
def chatbot():
    print("Hi I'm excited to chat with you")
chat_fun = Chat(instructions,reflections)       

if __name__ == "__main__":
    chatbot()
    chat_fun.converse()         #Converse method will help to initiate the conversation

