from sys import stdin

n = int(stdin.readline())
days = [0, 0, 0, 0, 0]
availability = []

daysCopied = []
dayNumbers = []
numOfBestDays = 0
bestDays = []

for a in range(n):
    availability.append(list(stdin.readline().strip("\n")))


for a in availability:
    for b in range(len(a)):
        if a[b] == "Y":
            days[b] += 1


daysCopied.extend(days)
days.sort(reverse = True)

for d in range(len(days)):
    for e in range(len(daysCopied)):
        if daysCopied[e] == days[d]:
            dayNumbers.append(e + 1)


for f in range(len(days)):
    if f == len(days) - 1:
        if days[f] == days[f - 1]:
            numOfBestDays += 1
    else:
        if days[f + 1] == days[f]:
            numOfBestDays += 1


for g in range(numOfBestDays):
    bestDays.append(dayNumbers[g])


bestDays.sort()
print(str(bestDays).strip("[]").replace(" ", ""))
