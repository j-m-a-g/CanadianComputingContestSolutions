from sys import stdin
m = int(stdin.readline())
n = int(stdin.readline())

sumsOfTen = 0

for a in range(1, m + 1):
    for b in range(1, n + 1):
        if a + b == 10:
            sumsOfTen += 1


if sumsOfTen == 1:
    print("There is " + str(sumsOfTen) + " way to get the sum 10.")
else:
    print("There are " + str(sumsOfTen) + " ways to get the sum 10.")
