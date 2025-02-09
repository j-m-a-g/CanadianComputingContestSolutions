from sys import stdin

b = int(stdin.readline())
p = 5 * b - 400
print(p)

if p > 100:
    print(-1)
elif p < 100:
    print(1)
else:
    print(0)
