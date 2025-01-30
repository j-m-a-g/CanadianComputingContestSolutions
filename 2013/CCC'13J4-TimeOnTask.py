totalTime = int(input())
numOfChores = int(input())

choreTimes = []

addedTimes = 0

for i in range(numOfChores):
    timeForChore = int(input())
    choreTimes.append(timeForChore)


choreTimes.sort()

for c in range(len(choreTimes)):
    addedTimes += choreTimes[c]
    if addedTimes > totalTime:
        print(c)
        break
