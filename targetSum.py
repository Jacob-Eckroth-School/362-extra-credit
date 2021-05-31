
def findSum(array,sumTarget):
    numberDict = {}
    for number in array:
        complement = sumTarget - number
        if(complement in numberDict):
            return [complement,number]  
        else:
            numberDict[number] = None
    return None

print(findSum([2,7,11,15],9))


