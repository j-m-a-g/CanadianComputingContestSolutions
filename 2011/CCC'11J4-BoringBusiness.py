from sys import stdin

positions = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]
currentPos = [-1, -5]
outputs = []

while True:
    currentCoordinate = stdin.readline().strip("\n").split()

    if currentCoordinate[0] != "q":
        if currentCoordinate[0] == "d":
            currentPos[1] = currentPos[1] - int(currentCoordinate[1])
        elif currentCoordinate[0] == "u":
            currentPos[1] = currentPos[1] + int(currentCoordinate[1])
        elif currentCoordinate[0] == "l":
            currentPos[0] = currentPos[0] - int(currentCoordinate[1])
        elif currentCoordinate[0] == "r":
            currentPos[0] = currentPos[0] + int(currentCoordinate[1])


        for p in positions:
            for a in range(len(p)):
                if currentPos[0] == p[0] and currentPos[1] > p[1]:
                    outputs.append(str(currentPos).strip("[]") + " DANGER")
                    break
                elif currentPos in positions:
                    outputs.append(str(currentPos).strip("[]") + " DANGER")
                    break
                else:
                    outputs.append(str(currentPos).strip("[]") + " safe")   
                    break
    else:
        break


for o in range(len(outputs)):
    try:
        if outputs[o] != outputs[o - 1]:
            print(str(outputs[o]).replace(",", ""))
        

        if str(outputs[o]).count("DANGER") >= 1:
            break
    except:
        break
