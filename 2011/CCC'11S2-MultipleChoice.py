from sys import stdin
correctAnswers = []
studentAnswers = []
numberOfCorrectAnswers = 0

n = int(stdin.readline())

for a in range(n):
    studentAnswers.append(stdin.readline().strip("\n"))
    
for b in range(n):
    correctAnswers.append(stdin.readline().strip("\n"))


for c in range(len(correctAnswers)):
    if correctAnswers[c] == studentAnswers[c]:
        numberOfCorrectAnswers += 1


print(numberOfCorrectAnswers)
