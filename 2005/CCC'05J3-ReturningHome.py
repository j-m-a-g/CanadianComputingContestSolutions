from sys import stdin
directions = []
newDirections = []
lastLine = ""

while True:
    currentDirection = stdin.readline().strip("\n")
    directions.append(currentDirection)

    if currentDirection == "SCHOOL":
        break
        


directions.reverse()
for a in range(len(directions)):
    if directions[a] == "L":
        try:
            newDirections.append("Turn RIGHT onto " + directions[a + 1] + " street.")
        except:
            break
    elif directions[a] == "R":
        try:
            newDirections.append("Turn LEFT onto " + directions[a + 1] + " street.")
        except:
            break
        

for n in newDirections:
    print(n)


if directions[-1] == "R":
    print("Turn LEFT into your HOME.")
else:
    print("Turn RIGHT into your HOME.")
