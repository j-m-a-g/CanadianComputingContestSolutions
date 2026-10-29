from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
K = int(stdin.readline())
T = int(stdin.readline())

startingHops = (B - A) // K
distanceFromLast = B - (K * startingHops)

if T == 2:
  print(startingHops + distanceFromLast)
else:
  nextMultiple = K * (startingHops + 1)
  additionalHops = nextMultiple - B

  print(startingHops + (nextMultiple // K) - additionalHops)
