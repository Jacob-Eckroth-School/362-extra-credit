import reverseSentence
import unittest



class sentenceTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverseSentence.reverseSentence("\n"),"\n")
    def test_example(self):
        self.assertEqual(reverseSentence.reverseSentence("My name is V Tadimeti\n"),"Tadimeti V is name My\n")
    def test_mytest(self):
        self.assertEqual(reverseSentence.reverseSentence("hi I'm Jacob\n"),"Jacob I'm hi\n")
    
if __name__ == "__main__":
    unittest.main()