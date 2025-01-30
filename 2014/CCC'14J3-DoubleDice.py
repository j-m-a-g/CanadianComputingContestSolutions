rounds = int(input())

AntoniaResults = []
DavidResults = []
Antonia = 100
David = 100

for r in range(rounds):
    singleRound = input()

    AntoniaResults.append(int(singleRound[0]))
    DavidResults.append(int(singleRound[2]))


for a in range(len(AntoniaResults)):
    if AntoniaResults[a] < DavidResults[a]:
        Antonia -= DavidResults[a]
    elif AntoniaResults[a] > DavidResults[a]:
        David -= AntoniaResults[a]


print(Antonia)
print(David)
