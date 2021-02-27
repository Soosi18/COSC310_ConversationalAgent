import nltk
from nltk.chat.util import Chat, reflections
print("Hello! This is The COSC310Chatbot. Feel free to ask any questions. To quit say a \"goodbye\" phrase")

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ], 
    [
        r"what is your name",
        ["You can call me The COSC310Chatbot.",]
    ],
    [
        r"how are you|how are you doing|how are you feeling",
        ["I am fine, thank you! How can I help you?",]
    ],
    [
        r"i am fine, thank you|i am fine|im fine|i'm fine|i am good, thank you|i am good|im good|i'm good",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"how can i help you",
        ["I am suppose to be helping you. So how can I help you",]
    ],
    [
        r"i'm doing good|i'm (.*) doing good",
        ["That's great to hear",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"goodbye|bye|take care|end|quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def chatbot():
        print("") 

chat = Chat(set_pairs, reflections)

chat.converse()
if __name__ == "__main__":
    chatbot()