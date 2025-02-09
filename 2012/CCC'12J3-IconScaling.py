from sys import stdin
k = int(stdin.readline())

for a in range(k):
    for b in range(k):
        print("*", end = "")
    for c in range(k):
        print("x", end = "")
    for d in range(k):
        print("*", end = "")
    print()


for e in range(k):
    for f in range(k):
        print(" ", end = "")
    for g in range(k):
        print("x", end = "")
    for h in range(k):
        print("x", end = "")
    print()


for i in range(k):
    for j in range(k):
        print("*", end = "")
    for l in range(k):
        print(" ", end = "")
    for m in range(k):
        print("*", end = "")
    print()
