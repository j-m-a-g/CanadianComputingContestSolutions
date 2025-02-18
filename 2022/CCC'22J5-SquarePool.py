from sys import stdin
import math

n = int(stdin.readline())
t = int(stdin.readline())
possibleDimensions = []

trees = []
for a in range(t):
    trees.append(stdin.readline().strip("\n").split())


for b in range(1, n + 1):
    for c in range(1, n + 1):
        for e in range(1, n + 1):
            topDifference = abs(c - 1)
            bottomDifference = abs((c + e) - topDifference - n)
            leftDifference = abs(b - 1)
            rightDifference = abs((b + e) - leftDifference - n)

            for t in trees:
                for d in range(len(t)):
                    try:
                        if int(t[d]) <= leftDifference or int(t[d]) >= rightDifference and int(t[d + 1]) <= topDifference or int(t[d + 1]) >= bottomDifference:
                            possibleDimensions.append(c)
                    except:
                        break


possibleDimensions.sort(reverse = True)
if possibleDimensions[0] >= 10:
    print(math.floor(possibleDimensions[0] / 2))
else:
    print(math.ceil(possibleDimensions[0] / 2))
