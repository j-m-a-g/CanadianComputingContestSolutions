from sys import stdin
n = int(stdin.readline())
outputs = []

for a in range(n):
    currentLine = stdin.readline().strip("\n").split()
    if int(currentLine[0]) * int(currentLine[1]) == int(currentLine[2]):
        outputs.append("POSSIBLE DOUBLE SIGMA")
    else:
        outputs.append("16 BIT S/W ONLY")


for o in outputs:
    print(o)
