import unittest
from piglatin import PigLatin
from error import PigLatinError
import logging


class TestPigLatin(unittest.TestCase):

    def test_inputPhrase(self):
        phrase="Hello World"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.get_phrase() == phrase)

    def test_EmptyPhrase(self):
        phrase=""
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate() == "nil")

    def test_vowelsAny(self):
        phrase="any"
        phrase2="apple"
        phrase3="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate() == "anynay")

    def test_vowelsApple(self):
        phrase="apple"
        phrase3="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate() == "appleyay")

    def test_vowelsAsk(self):
        phrase="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate() == "askay")

    def test_consonants(self):
        phrase="known"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate() == "ownknay")

    
