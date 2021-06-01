import re


def reverseSentence(sentenceToBeReversed):
    sentenceHasNewline = False
    if(len(sentenceToBeReversed) > 0):
        if sentenceToBeReversed[len(sentenceToBeReversed)-1] == '\n':
            sentenceHasNewline = True
    splitWords = re.split('\s',sentenceToBeReversed)

    splitWords.reverse()
    while '' in splitWords:
        splitWords.remove('')

    newSentence = ""
    
    for i in range(len(splitWords)):
        newSentence += splitWords[i]
        if(i != len(splitWords)-1):      #If we're not at the last word
            newSentence += " "
    if sentenceHasNewline:
        newSentence += '\n'
    return newSentence

def main():
    userInput = input('Please enter a sentence with multiple words to be reversed:')
    reversedInput = reverseSentence(userInput)
    print("That sentence reversed is:",reversedInput)


if __name__ == "__main__":
    main()