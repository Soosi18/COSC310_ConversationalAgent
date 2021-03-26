#Unit Testing
import unittest
import chatbot
from load import load

class TestChatbot(unittest.TestCase):
    
    def setUp(self):
        self.l = load("intents.json")
        self.data = self.l.getData()
        for t in self.data["intents"]:
            if t['tag'] == "greeting":
                self.responses = t['responses']
            if t["tag"] =="music":
                self.responsesmusic = t['responses']
        #pass

    def tearDown(self):
        pass

    def test_chat(self):                
        self.assertTrue(chatbot.chat("How are you") in self.responses)
    
    def test_tag(self):
        chatbot.chat("How are you")
        self.assertEqual(chatbot.tag,"greeting")

    def test_sentiment(self):
        self.assertEqual(chatbot.chat("I love your work"),"Glad to hear you really like that.")
        self.assertEqual(chatbot.chat("I hate you"),"I can understand that.")
        self.assertEqual(chatbot.chat("I like this conversation"),"I fully agree.")

    def test_capitalization(self):
        self.assertTrue(chatbot.chat("hOW aRE yOU") in self.responses)
        self.assertTrue(chatbot.chat("HOW ARE YOU") in self.responses)
        self.assertTrue(chatbot.chat("how are you") in self.responses)

    def test_punctuation(self):
        self.assertTrue(chatbot.chat("how are you.") in self.responses)
        self.assertTrue(chatbot.chat("how are you!") in self.responses)
        self.assertTrue(chatbot.chat("how are you?") in self.responses)

    def test_synonyms(self):
        self.assertTrue(chatbot.chat("what type of music do you listen to") in self.responsesmusic)
        self.assertTrue(chatbot.chat("what tunes do you listen to") in self.responsesmusic)

        


if __name__ == '__main__':
    unittest.main()