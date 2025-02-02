import sys
sys.setrecursionlimit(1000000)

number = int(input())

def checkIfApplicable():
    global number

    number += 1 
    numberArray = list(str(number))

    for n in numberArray:
        if n == "0":
            checkIfApplicable()

    return number


print(checkIfApplicable())
