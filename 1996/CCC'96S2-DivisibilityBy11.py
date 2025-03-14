from sys import stdin
n = int(stdin.readline())
outputs = []

for a in range(n):
    concatenated = ""
    currentNumber = list(stdin.readline().strip("\n"))

    for c in currentNumber:
        concatenated += c

    onesDigit = int(currentNumber[-1])
    currentNumber[-1] = ""
    
    outputs.append(int(concatenated) - onesDigit)


for o in outputs:
    print(o)
