import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_inputPhrase(self):
        phrase="Hello World"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.get_phrase(phrase) == phrase)

    def test_EmptyPhrase(self):
        phrase=""
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate(phrase) == "nil")

    def test_vowelsAny(self):
        phrase="any"
        phrase2="apple"
        phrase3="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate(phrase) == "anynay")

    def test_vowelsApple(self):
        phrase="apple"
        phrase3="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate(phrase) == "appleyay")

    def test_vowelsAsk(self):
        phrase="ask"
        translator = PigLatin(phrase) 
        self.assertTrue(translator.translate(phrase) == "askay")

    def test_consonants(self):
        phrase="known"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "ownknay")

    def test_words(self):
        phrase="hello world"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "ellohay orldway")

    def test_compositeWords(self):
        phrase="well-being"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "ellway-eingbay")

    def test_punctuation(self):
        phrase="hello world!"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "ellohay orldway!")  

    def test_invalidPunctuation(self):
        phrase="hello world$"
        translator = PigLatin(phrase)
        self.assertRaises(PigLatinError, translator.translate(phrase))

    def test_uppeCase(self):
        phrase="APPLE"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "APPLEYAY") 

    def test_titleCase(self):
        phrase="Hello"
        translator = PigLatin(phrase)
        self.assertTrue(translator.translate(phrase) == "Ellohay")  

    def test_invalidCase(self):
        phrase="hEllO"
        translator = PigLatin(phrase)
        self.assertRaises(PigLatinError, translator.translate(phrase))

    
    
