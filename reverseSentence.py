import re


def reverseSentence(sentenceToBeReversed):
    splitWords = re.split('\s',sentenceToBeReversed)

    splitWords.reverse()
    while '' in splitWords:
        splitWords.remove('')

    newSentence = ""
    
    for i in range(len(splitWords)):
        newSentence += splitWords[i]
        if(i != len(splitWords)-1):      #If we're not at the last word
            newSentence += " "
    newSentence += '\n'
    return newSentence

def main():
    userInput = input('Please enter a sentence with multiple words to be revsered:')
    reversedInput = reverseSentence(userInput)
    print("That sentence reversed is:",reversedInput)


if __name__ == "__main__":
    main()