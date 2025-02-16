from sys import stdin
outputs = []
n = int(stdin.readline())

for a in range(n):
    currentLine = stdin.readline().strip("\n").split()
    outputs.append(int(currentLine[0]) + int(currentLine[1]))


for o in outputs:
    print(o)
