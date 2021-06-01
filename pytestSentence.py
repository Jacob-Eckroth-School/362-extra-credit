import reverseSentence


def test_empty():
    assert reverseSentence.reverseSentence("\n") == "\n"

def test_example():
   assert reverseSentence.reverseSentence("My name is V Tadimeti\n") =="Tadimeti V is name My\n"
def test_mytest():
    assert reverseSentence.reverseSentence("hi I'm Jacob\n") =="Jacob I'm hi\n"