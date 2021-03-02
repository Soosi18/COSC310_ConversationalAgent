from load import load
import numpy
import random

l = load("intents.json")
data = l.getData()
l.Process()
model = l.getModel()
words = l.getWords()
labels = l.getLabels()


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([l.bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        #print(results)
        if results[results_index] > 0.8:
            for t in data["intents"]:
                if t['tag'] == tag:
                    responses = t['responses']

            print(random.choice(responses))
        else:
            print("I didn't quite understand")

chat()
