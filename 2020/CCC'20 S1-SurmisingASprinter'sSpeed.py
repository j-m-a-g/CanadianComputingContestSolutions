from sys import stdin
n = int(stdin.readline())

timeAndDistance = []
timeAndDistanceInt = []
times = []
distances = []
speeds = []

for a in range(n):
    currentLine = stdin.readline().strip("\n").split()

    timeAndDistance.append(currentLine)


for t in timeAndDistance:
    currentArray = []
    for b in t:
        currentArray.append(int(b))
    
    timeAndDistanceInt.append(currentArray)


timeAndDistanceInt.sort()

for i in timeAndDistanceInt:
    for c in range(len(i)):
        times.append(i[c])
        distances.append(i[c + 1])
        break


for d in range(len(times)):
    try:
        timeDifference = abs(times[d] - times[d + 1])
        distanceDifference = abs(abs(distances[d]) - abs(distances[d + 1]))
        speeds.append(distanceDifference / timeDifference)
    except:
        break


speeds.sort()
print(speeds[-1])
