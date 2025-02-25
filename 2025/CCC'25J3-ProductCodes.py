from sys import stdin
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")

n = int(stdin.readline())
outputs = []

for a in range(n):
    concatenated = ""
    integers = []
    sum = 0
    currentString = list(stdin.readline().strip("\n"))

    for b in range(len(currentString)):
        if currentString[b] in lowercase:
            currentString[b] = ""


    for c in range(len(currentString)):
        if currentString[c] in numbers:
            concatenated += currentString[c]
        elif currentString[c] == "-" and currentString[c - 1] in numbers:
            integers.append(concatenated)
            concatenated = "-"
        elif currentString[c] == "-" and currentString[c + 1] in numbers:
            concatenated += currentString[c]
        else:
            integers.append(concatenated)
            concatenated = ""

        if c == len(currentString) - 1:
            integers.append(concatenated)


    for d in range(len(currentString)):
        if currentString[d] in numbers or currentString[d] == "-":
            currentString[d] = ""


    for i in integers:
        try:
            sum += int(i)
        except:
            pass


    concatenatedList = []
    for j in currentString:
        if j != "":
            concatenatedList.append(j)


    concatenatedList.append(sum)
    outputs.append(concatenatedList)


for o in outputs:
    for p in o:
        print(p, end="")
    
    print()
