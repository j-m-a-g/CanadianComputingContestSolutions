from sys import stdin
currentPos = 1
outputs = []

while True:
    currentMove = int(stdin.readline())
    
    if currentMove == 0:
        outputs.append("You Quit!")
        break
    else:
        currentPos += currentMove

        if currentPos == 9:
            currentPos = 34
        elif currentPos == 54:
            currentPos = 19
        elif currentPos == 40:
            currentPos = 64
        elif currentPos == 90:
            currentPos = 48
        elif currentPos == 67:
            currentPos = 86
        elif currentPos == 99:
            currentPos = 77
        elif currentPos > 100:
            currentPos -= currentMove
        elif currentPos == 100:
            outputs.append("You are now on square " + str(currentPos))
            outputs.append("You Win!")
            break

        outputs.append("You are now on square " + str(currentPos))


for o in outputs:
    print(o)
