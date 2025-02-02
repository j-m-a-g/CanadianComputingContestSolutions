from math import sqrt
from math import cbrt
from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
coolNumbers = 0

if a != b:
    for i in range(a, b):
        if sqrt(i).is_integer() and cbrt(i).is_integer():
            coolNumbers += 1
else:
    if sqrt(a).is_integer() and cbrt(a).is_integer():
        coolNumbers += 1


print(coolNumbers)
