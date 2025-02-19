from sys import stdin

canvas = []
gold = 0
m = int(stdin.readline())
n = int(stdin.readline())
k = int(stdin.readline())

for a in range(m):
    currentRow = []
    for b in range(n):
        currentRow.append("B")

    canvas.append(currentRow)

for c in range(k):
    currentLine = stdin.readline().strip("\n").split()
    if currentLine[0] == "C":
        for d in range(len(canvas)):
            if canvas[d][int(currentLine[1]) - 1] == "G":
                canvas[d][int(currentLine[1]) - 1] = "B"
            else:
                canvas[d][int(currentLine[1]) - 1] = "G"
    elif currentLine[0] == "R":
        for d in range(len(canvas[int(currentLine[1]) - 1])):
            if canvas[int(currentLine[1]) - 1][d] == "G":
                canvas[int(currentLine[1]) - 1][d] = "B"
            else:
                canvas[int(currentLine[1]) - 1][d] = "G"

for f in canvas:
    for g in f:
        if g == "G":
            gold += 1

print(gold)
