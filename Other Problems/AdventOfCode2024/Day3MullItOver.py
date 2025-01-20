workingFile = "Other Problems\\AdventOfCode2024\\day3Input.txt"
day3Input = open(workingFile, "r")
loopRange = 0

with day3Input as lines:
    loopRange = len(lines.readlines())
    

day3Input = open(workingFile, "r")

inputList = list(day3Input.readline().replace("\n", ""))
multipliedIntegerProducts = []
multipliedIntegers = 0

firstInt = 0
secondInt = 0
    
for i in range(len(inputList)):
    if inputList[i - 3] == "m" and inputList[i - 2] == "u" and inputList[i - 1] == "l" and inputList[i] == "(":
        # X,Y
        if inputList[i + 5] == "," and inputList[i + 7] == ")":
            firstInt = inputList[i + 4]
            secondInt = inputList[i + 6]
        # X,YY
        elif inputList[i + 5] == "," and inputList[i + 8] == ")":
            firstInt = inputList[i + 4]
            secondInt = str(inputList[i + 6] + inputList[i + 7])
        # X,YYY
        elif inputList[i + 5] == "," and inputList[i + 9] == ")":
            firstInt = inputList[i + 4]
            secondInt = str(inputList[i + 6] + inputList[i + 7] + inputList[i + 8])
        # XX,Y
        elif inputList[i + 6] == "," and inputList[i + 8] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            secondInt = inputList[i + 7]
        # XX,YY
        elif inputList[i + 6] == "," and inputList[i + 9] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            secondInt = str(inputList[i + 7] + inputList[i + 8])
        # XX,YYY
        elif inputList[i + 6] == "," and inputList[i + 10] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            secondInt = str(inputList[i + 7] + inputList[i + 8] + inputList[i + 9])
        # XXX,Y
        elif inputList[i + 7] == "," and inputList[i + 9] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            secondInt = inputList[i + 8]
        # XXX,YY
        elif inputList[i + 7] == "," and inputList[i + 10] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            secondInt = str(inputList[i + 8] + inputList[i + 9])
        # XXX,YYY
        elif inputList[i + 7] == "," and inputList[i + 11] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            secondInt = str(inputList[i + 8] + inputList[i + 9] + inputList[i + 10])
    
        
        multipliedIntegers = int(firstInt) * int(secondInt)
        multipliedIntegerProducts.append(multipliedIntegers)
    else:
        print(inputList[i])
        
        
print(inputList)
print(sum(multipliedIntegerProducts))
