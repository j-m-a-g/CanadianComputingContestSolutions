from sys import stdin

h = int(stdin.readline())
m = int(stdin.readline())
a = 1
t = 0

while a > 0:
    t += 1
    a = -6 * (t ** 4) + h * (t ** 3) + 2 * (t ** 2) + t


if t > m:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:")
    print(t)
