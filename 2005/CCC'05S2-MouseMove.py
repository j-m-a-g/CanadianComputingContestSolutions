from sys import stdin
currentPos = [0, 0]
positions = []
screenDimensions = stdin.readline().strip("\n").split()

while True:
    currentMove = stdin.readline().strip("\n").split()

    if currentMove != ["0", "0"]:
        xMovement = currentPos[0] + int(currentMove[0])
        yMovement = currentPos[1] + int(currentMove[1])
        
        if xMovement < 0:
            currentPos = [0, yMovement]
        elif yMovement < 0:
            currentPos = [xMovement, 0]
        elif xMovement < 0 and yMovement < 0:
            currentPos = [0, 0]
        elif xMovement > int(screenDimensions[0]):
            currentPos = [int(screenDimensions[0]), yMovement]
        elif yMovement > int(screenDimensions[1]):
            currentPos = [xMovement, int(screenDimensions[1])]
        elif xMovement > int(screenDimensions[0]) and yMovement > int(screenDimensions[1]):
            currentPos = [screenDimensions[0], screenDimensions[1]]
        elif xMovement > int(screenDimensions[0]) and yMovement < 0:
            currentPos = [int(screenDimensions[0]), 0]
        elif xMovement < 0 and yMovement > int(screenDimensions[1]):
            currentPos = [0, int(screenDimensions[1])]
        else:
            currentPos = [xMovement, yMovement]

        positions.append(currentPos)
    else:
        break


for p in positions:
    print(str(p).strip("[]").replace(",", ""))
