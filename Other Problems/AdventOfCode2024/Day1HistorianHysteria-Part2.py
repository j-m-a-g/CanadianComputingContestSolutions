workingFile = "Other Problems\AdventOfCode2024\locationIDs.txt"

# Test Case
#workingFile = "Other Problems\AdventOfCode2024\orderedIDs.txt"
locationIdList = open(workingFile, "r")

loopRange = 0

with locationIdList as lines:
    loopRange = len(lines.readlines())
    

locationIdList = open(workingFile, "r")

firstNumList = []
secondNumList = []

for i in range(loopRange):
    locationIdListResult = list(locationIdList.readline())
    
    # Example test case
    #firstNum = locationIdListResult[0]
    #secondNum = locationIdListResult[4]
    
    firstNum = locationIdListResult[0] + locationIdListResult[1] + locationIdListResult[2] + locationIdListResult[3] + locationIdListResult[4]
    secondNum = locationIdListResult[8] + locationIdListResult[9] + locationIdListResult[10] + locationIdListResult[11] + locationIdListResult[12]
    
    firstNumList.append(firstNum)
    secondNumList.append(secondNum)
    

firstNumList.sort()
secondNumList.sort()

print(firstNumList)
print(secondNumList)

factorCounter = 0

combinedInt = []
combinedFactors = []
    
for length in range(loopRange):
    if (firstNumList[length] == secondNumList[length]):
        factorCounter = factorCounter + 1
        combinedInt.append(firstNumList[length])
        combinedFactors.append(factorCounter)
    # else:
    #     if (firstNumList[r + 1] == secondNumList[r + 1]):
    #         factorCounterParallel += 1
    #         combinedFactors.append(factorCounterParallel)


print(combinedInt)
print(combinedFactors)
