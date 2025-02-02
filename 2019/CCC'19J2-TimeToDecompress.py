lines = int(input())

lineArray = []
timesToDisplay = []
symbols = []

for a in range(lines):
    lineArray.append(input())


for line in lineArray:
    for b in range(len(line)):
        if len(line) > 3:
            try:
                timesToDisplay.append(line[b] + line[b + 1])
                symbols.append(line[b + 3])
                break
            except:
                break
        else:
            try:
                timesToDisplay.append(line[b] + line[b + 1])
                symbols.append(line[b + 2])
                break
            except:
                break


for t in range(len(timesToDisplay)):
    for s in range(int(timesToDisplay[t])):
        print(symbols[t], end = "")


    print()
