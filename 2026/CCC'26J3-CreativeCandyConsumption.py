from sys import stdin

NgocEaten = 0
MinhEaten = 0

upperBound = 0
lowerBound = 0

NgocCandy = list(stdin.readline())
MinhCandy = list(stdin.readline())

NgocCandy.remove("\n")
MinhCandy.remove("\n")

"""
if len(NgocCandy) > len(MinhCandy):
  upperBound = len(NgocCandy)
  lowerBound = len(MinhCandy)
else:
  upperBound = len(MinhCandy)
  lowerBound = len(NgocCandy)
"""

for a in range(len(NgocCandy)):
  if NgocCandy[a] == MinhCandy[a]:
    NgocEaten += 1
    NgocCandy.pop(a)

    MinhEaten += 1
    MinhCandy.pop(a)
    
    a -= 1
  elif NgocCandy[a] == "R" and MinhCandy[a] == "G":
    NgocEaten += 1
    MinhCandy.pop(a)
    a -= 1
  elif MinhCandy[a] == "R" and NgocCandy[a] == "G":
    MinhEaten += 1
    NgocCandy.pop(a)
    a -= 1
  elif NgocCandy[a] == "G" and MinhCandy[a] == "B":
    NgocEaten += 1
    MinhCandy.pop(a)
    a -= 1
  elif MinhCandy[a] == "G" and NgocCandy[a] == "B":
    MinhEaten += 1
    NgocCandy.pop(a)
    a -= 1
  elif NgocCandy[a] == "B" and MinhCandy[a] == "R":
      NgocEaten += 1
      MinhCandy.pop(a)
      a -= 1
  elif MinhCandy[a] == "B" and NgocCandy[a] == "R":
      MinhEaten += 1
      NgocCandy.pop(a)
      a -= 1

print(NgocEaten)
print(MinhEaten)
