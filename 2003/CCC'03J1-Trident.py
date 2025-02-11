from sys import stdin
import math
t = int(stdin.readline())
s = int(stdin.readline())
h = int(stdin.readline())

for a in range(t):
    for b in range(3):
        print("*", end="")
        for c in range(s):
            print(" ", end="")

    print()


middleLength = 3 + 2 * s

for d in range(middleLength):
    print("*", end="")


print()
middleOfMiddle = math.floor(middleLength / 2)
for e in range(h):
    for f in range(middleOfMiddle):
        print(" ", end="")
    
    print("*")
