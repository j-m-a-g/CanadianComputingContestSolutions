N = int(input())

scoreArray = []

for i in range(N):
    eachScore = int(input())
    scoreArray.append(eachScore)


scoreArray.sort(reverse = True)

goldScore = scoreArray[0]
bronzeScore = 0

for g in range(N):
    if scoreArray[g] == goldScore:
        scoreArray[g] = -1


scoreArray.sort(reverse = True)
silverScore = scoreArray[0]
for s in range(N):
    if scoreArray[s] == silverScore:
        scoreArray[s] = -1


scoreArray.sort(reverse = True)

bronzeCount = 0
for b in scoreArray:
    if b != -1 and b == scoreArray[0]:
        bronzeCount += 1


print(scoreArray[0], bronzeCount)
