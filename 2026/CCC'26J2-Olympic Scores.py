from sys import stdin

sumOfScores = 0
scores = []

for a in range(5):
  currentInput = int(stdin.readline())
  scores.append(currentInput)

D = int(stdin.readline())

scores.sort()
scores.pop(0)
scores.pop(3)

for b in range(len(scores)):
  sumOfScores += scores[b]

print(sumOfScores * D)
