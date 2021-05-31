
def findSum(array,sumTarget):
    numberDict = {}
    for number in array:
        complement = sumTarget - number
        if(complement in numberDict):
            return [number,complement]  
        else:
            numberDict[number] = None
    return None




