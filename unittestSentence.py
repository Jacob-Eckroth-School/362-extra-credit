import reverseSentence
import unittest



class sentenceTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverseSentence.reverseSentence(""),"")
    def test_example(self):
        self.assertEqual(reverseSentence.reverseSentence("My name is V Tadimeti"),"Tadimeti V is name My")
    def test_mytest(self):
        self.assertEqual(reverseSentence.reverseSentence("hi I'm Jacob"),"Jacob I'm hi")
    
if __name__ == "__main__":
    unittest.main()