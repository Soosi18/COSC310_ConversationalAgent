import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

class load:
    def __init__(self,f):
        with open(f) as file:
            data = json.load(file)
        self.data = data
    

    def Process(self):
        try:
            with open("data.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            words =  []
            labels = []
            docs_x = []
            docs_y = []
            data = self.data

            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])
            ignore_words = ['?', '.', '!']
            words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
            words = sorted(list(set(words)))

            labels = sorted(labels)

            training = []
            output = []

            out_empty = [0 for _ in range(len(labels))]

            for x, doc in enumerate(docs_x):
                bag = []

                wrds = [stemmer.stem(w.lower()) for w in doc]

                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(output_row)


            training = numpy.array(training)
            output = numpy.array(output)

            with open("data.pickle", "wb") as f:
                pickle.dump((words, labels, training, output), f)

        tensorflow.compat.v1.reset_default_graph()

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)
        
        
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save("model.tflearn")
        self.words = words
        self.model = model
        self.labels = labels



    def bag_of_words(self,s,words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
            
        return numpy.array(bag)

    def getData(self):
        return self.data

    def getModel(self):
        return self.model

    def getWords(self):
        return self.words
    
    def getLabels(self):
        return self.labels

   