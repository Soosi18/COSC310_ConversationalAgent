#This file contains the actual chat function of the bot and focuses on the input and output
#If need be, chatbot calls load.py to load in all the data that it needs to run
<<<<<<< .merge_file_a17776
from load import load  #import load function from load.py
import numpy           #numpy for use of numpy.argmax 
import random          #random for grabbing a random response from the matching tag
<<<<<<< HEAD
from nltk.corpus import wordnet as wn 
from pycorenlp import StanfordCoreNLP
import nltk
=======
from load import load           #import load function from load.py
from sentiment import sentiment #import sentiment function from sentiment.py
import numpy                    #numpy for use of numpy.argmax 
import random                   #random for grabbing a random response from the matching tag
>>>>>>> .merge_file_a03716
=======
from syn_recognition import synonym_sentences
>>>>>>> sarvagya_gui_pos_syn

#load in the json file
l = load("intents.json")
#save all data and tflearn models to use when calculating probabilites
data = l.getData()
l.Process()
model = l.getModel()
words = l.getWords()
labels = l.getLabels()

<<<<<<< .merge_file_a17776

#This method takes in user input from the Entry box in the GUI, and returns an appropriate response from the bot.
def chat(user_inp, *args):
    while True:
        #Run every sentence with different synonym combinations till one is recognized
        sentence_list = synonym_sentences(user_inp)
        for inp in sentence_list:
            print(inp)
=======
#for now this method prints out the response, but once we implment a gui, it should return the response instead
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        #instantiates sentiment object
        s = sentiment(inp)
        #determines if input is not a sentiment
        if(s.isNotSentiment()):
>>>>>>> .merge_file_a03716
            #results will hold the predicted value of the tags in corrispondence with the user's input    
            results = model.predict([l.bag_of_words(inp, words)])[0]
            #Grab the highest result and store it in results_index
            results_index = numpy.argmax(results)
<<<<<<< .merge_file_a17776
            #Grab the tag belonging to the highest result
            tag = labels[results_index]
            #Un-comment the code below to see the probability % of each tag that matches in results, and the tag that has the max probability.
            #print(results)
            #print(tag)

            #Check if the probability is higher than a set amount. We use 0.8 here to determine if we want to bot to give a random
=======
            #we then can grab the tag belonging to the highest result
            tag = labels[results_index]
            #You can run the below line to see the probability % of each tag that matches in results, and the tag that has the max probability.
            #print(results)
            #print(tag)

            #Check if the probablitu is higher than a set amount, we use 0.8 here to determine if we want to bot to give a random
>>>>>>> .merge_file_a03716
            #response or for it to say "it didn't understand"
            if results[results_index] > 0.8:
                for t in data["intents"]:
                    if t['tag'] == tag:
                        responses = t['responses']

<<<<<<< .merge_file_a17776
                return random.choice(responses)

        return "I didn't quite understand"




<<<<<<< HEAD
    # Use the API to POS-tag the sentence and get a json file back as output
    output = nlp.annotate(sentence, properties = 
    {
        'annotators': 'pos',
        'outputFormat': 'json',
    })
    
    # list_replacements will contain all important words that we will find synonyms for. If word matches the POS tag, add it to the list.
    # Run a loop that iterates over each word in the sentence we take in as input.
    # POS-tags: NN - Noun(Singular), NNS - Noun(Plural), UH - Exclamation/Greeting, VB - Verb
    list_replacements = []
    for sent in output['sentences']:
        for word in sent['tokens']:
            if word['pos'] == 'NNS' or word['pos'] == 'NN' or word['pos'] == 'UH' or word['pos'] == 'VB':
                list_replacements.append(word['word'])

    # If no useful words found, return list containing only user's initial input sentence.
    if list_replacements == None:
        return sentence_list
    
    # For each replacable word, find synsets. If they don't exist, return user's initial sentence.
    for word in list_replacements:
        syn = wn.synsets(word)
        if syn is None:
            return sentence_list

        # For each synonym in the synset, find hypernyms(Broader-category words) and hyponyms(more specific words) and add them to their own lists.
        # If they dont exist, keep their lists empty to avoid crashes.
        for each_syn in syn:
            try:
                list_hypernyms = each_syn.hypernyms()
                list_hyponyms = each_syn.hyponyms()
            except:
                list_hypernyms = []
                list_hyponyms = []

            # list_newwords contains lists of hyper/hyponyms and words similar to them that we are going to use to replace the original words in the sentence.
            list_newwords = []
            for hyponym in list_hyponyms:
                list_newwords.append(hyponym.lemma_names())

            for hypernym in list_hypernyms:
                list_newwords.append(hypernym.lemma_names())
            # Replacing original sentence with new words and adding it to sentences_list
            for list in list_newwords:
                for newword in list:
                    if "_" in newword:
                        newword = newword.replace("_", " ")
                    sentence_list.append(sentence.replace(word, newword))
=======
                print(random.choice(responses))
            else:
                print("I didn't quite understand")
        else:
            sent = s.sentiment_analysis()
            s.sentimentNumber(sent)

#call chat function
chat()
>>>>>>> .merge_file_a03716

    # Return sentences_list containing many different sentences with different combinations of synonyms
    return sentence_list
=======
>>>>>>> sarvagya_gui_pos_syn
    
