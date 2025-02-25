import math
from sys import stdin

n = int(stdin.readline())
streams = []

for a in range(n):
    streams.append(int(stdin.readline()))

while True:
    currentLine = int(stdin.readline())

    if currentLine == 99:
        streamToBeSplit = int(stdin.readline()) - 1
        portion = int(stdin.readline())

        currentFlow = streams[streamToBeSplit]
        remainingFlow = streams[streamToBeSplit] * (portion / 100)
        streams[streamToBeSplit] = remainingFlow
        if streamToBeSplit < len(streams) - 1:
            streams.insert(streamToBeSplit + 1, currentFlow - remainingFlow)
    elif currentLine == 88:
        rejoin = int(stdin.readline()) - 1
        if rejoin < len(streams) - 1:
            streams[rejoin] = streams[rejoin] + streams[rejoin + 1]
            streams[rejoin + 1] = ""
    elif currentLine == 77:
        break

for s in streams:
    print(math.floor(s), end=" ")
