from sys import stdin

n = int(stdin.readline())
c = int(stdin.readline())
p = int(stdin.readline())

peopleAbleToRide = c * p
if n > peopleAbleToRide:
    print("no")
else:
    print("yes")
