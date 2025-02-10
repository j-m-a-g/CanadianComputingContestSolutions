from sys import stdin
import math

n = int(stdin.readline())
if n >= 1111:
    secondButtonClicks = n / 1111
    if secondButtonClicks.is_integer():
        print(math.floor(secondButtonClicks))
    else:
        secondButtonClicks = math.floor(secondButtonClicks)
        remainingClicks = n - secondButtonClicks * 1111
        print(remainingClicks + secondButtonClicks)
else:
    print(n)
