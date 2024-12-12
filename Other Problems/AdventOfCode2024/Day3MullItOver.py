workingFile = "Other Problems\\AdventOfCode2024\\day3Input.txt"
day3Input = open(workingFile, "r")
loopRange = 0

with day3Input as lines:
    loopRange = len(lines.readlines())
    

day3Input = open(workingFile, "r")

inputList = list(day3Input.readline().replace("\n", ""))
multipliedIntegerProducts = []
multipliedIntegers = 0
    
for i in range(len(inputList)):
    if inputList[i] == "m" and inputList[i + 1] == "u" and inputList[i + 2] == "l" and inputList[i + 3] == "(":
        # X, Y
        if inputList[i + 5] == "," and inputList[i + 7] == ")":
            multipliedIntegers = int(inputList[i + 4]) * int(inputList[i + 6])
        # X, YY
        elif inputList[i + 5] == "," and inputList[i + 8] == ")":
            secondInt = str(inputList[i + 6] + inputList[i + 7])
            multipliedIntegers = int(inputList[i + 4]) * int(secondInt)
        # X, YYY
        elif inputList[i + 5] == "," and inputList[i + 9] == ")":
            secondInt = str(inputList[i + 6] + inputList[i + 7] + inputList[i + 8])
            multipliedIntegers = int(inputList[i + 4]) * int(secondInt)
        # XX, Y
        elif inputList[i + 6] == "," and inputList[i + 8] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            multipliedIntegers = int(firstInt) * int(inputList[i + 7])
        # XX, YY
        elif inputList[i + 6] == "," and inputList[i + 9] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            secondInt = str(inputList[i + 7] + inputList[i + 8])
            multipliedIntegers = int(firstInt) * int(secondInt)
        # XX, YYY
        elif inputList[i + 6] == "," and inputList[i + 10] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5])
            secondInt = str(inputList[i + 7] + inputList[i + 8] + inputList[i + 9])
            multipliedIntegers = int(firstInt) * int(secondInt)
        # XXX, Y
        elif inputList[i + 7] == "," and inputList[i + 9] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            multipliedIntegers = int(firstInt) * int(inputList[i + 8])
        # XXX, YY
        elif inputList[i + 7] == "," and inputList[i + 10] == ")":
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            secondInt = str(inputList[i + 8] + inputList[i + 9])
            multipliedIntegers = int(firstInt) * int(secondInt)
        # XXX, YYY
        elif inputList[i + 7] == "," and inputList[i + 11]:
            firstInt = str(inputList[i + 4] + inputList[i + 5] + inputList[i + 6])
            secondInt = str(inputList[i + 8] + inputList[i + 9] + inputList[i + 10])
            multipliedIntegers = int(secondInt) * int(secondInt)
    
    
        multipliedIntegerProducts.append(multipliedIntegers)
    else:
        print("Wrong")
        
        
print(inputList)
print(sum(multipliedIntegerProducts))
