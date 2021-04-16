import wikipedia #import wikipedia API features
import random
import re


def choosedef(tag, ip):
    if (tag == "definition"):
        out = definition(ip)

    elif (tag == "importantpolitics"):
        out = politicalterms()

    return out

# Returns the definition of a random word or phrases from the set of phrases stored in the list 'terms'.
def politicalterms():
    terms = ["Justin Trudeau", "Liberal Party of Canada", "Pierre Trudeau", "Conservative Party of Canada", "Parliament of Canada", "House of Commons of Canada", "Prime Minister of Canada",
    "Foreign Relations of Canada", "44th Canadian federal election"
    ]
    word = random.choice(terms)
    try:
        return "Here is the definition of '" + word + "':\n\n" + wikipedia.summary(word, sentences = 3) + "\n\n Hope you learned something from that!\n"
    except:
        return "I can't think of anything right now, ask me later"    

# This function returns the definition of the word between the apostrophes in user's input. If definition is not found, returns an error message.
def get_definition(ip):
    word = ""
    for char in ip:
        if char == "'":
            word = ip[ip.index(char):]
            word = word.replace("?", "")
            return word

    return word

def definition(ip):
    word = get_definition(ip)
    try:
        return "Here is the definition of " + word + ":\n\n" + wikipedia.summary(word, sentences = 3) + "\n\nHope that was helpful!\n"
    except:
        return "Sorry, I couldn't find a definition for " + word + ". Please try again with another word.\n"
