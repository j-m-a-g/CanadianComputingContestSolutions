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
    
differences = []

for length in range(len(firstNumList)):
     currentDifference = abs(int(secondNumList[length]) - int(firstNumList[length]))
     differences.append(currentDifference)


print(differences)
print(sum(differences))
