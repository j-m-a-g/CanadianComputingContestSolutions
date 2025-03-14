from sys import stdin
n = int(stdin.readline())
outputs = []

for a in range(n):
    currentLine = list(stdin.readline().strip("\n"))

    outputList = []
    character = currentLine[0]
    count = 1
    for b in range(len(currentLine)):
        if b < len(currentLine) - 1:
            if currentLine[b + 1] == character:
                count += 1
            else:
                outputList.append(str(count) + " " + character + " ")
                count = 1
                character = currentLine[b + 1]
        else:
            outputList.append(str(count) + " " + character + " ")


    outputs.append(outputList)


for o in outputs:
    for p in o:
        print(p, end="")

    print()
