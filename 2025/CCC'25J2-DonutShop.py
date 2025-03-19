from sys import stdin

d = int(stdin.readline())
e = int(stdin.readline())

for a in range(e):
    eventSign = stdin.readline().strip("\n")
    eventAmount = int(stdin.readline())

    if eventSign == "-":
        d -= eventAmount
    else:
        d += eventAmount

print(d)
