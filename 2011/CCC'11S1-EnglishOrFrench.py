n = int(input())
TCount = 0
SCount = 0

for a in range(n):
    currentLine = list(input())

    for c in currentLine:
        if c in ["t", "T"]:
            TCount += 1
        elif c in ["s", "S"]:
            SCount += 1


if TCount > SCount:
    print("English")
elif TCount < SCount:
    print("French")
elif TCount == SCount:
    print("French")
