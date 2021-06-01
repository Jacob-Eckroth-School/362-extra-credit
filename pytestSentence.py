import reverseSentence


def test_empty():
    assert reverseSentence.reverseSentence("") == ""

def test_example():
   assert reverseSentence.reverseSentence("My name is V Tadimeti") =="Tadimeti V is name My"
def test_mytest():
    assert reverseSentence.reverseSentence("hi I'm Jacob") =="Jacob I'm hi"