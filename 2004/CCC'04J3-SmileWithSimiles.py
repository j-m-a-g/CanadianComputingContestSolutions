numOfAdjectives = int(input())
numOfNouns = int(input())

adjectives = []
nouns = []

for a in range(numOfAdjectives):
    currentAdjective = input()
    adjectives.append(currentAdjective)


for b in range(numOfNouns):
    currentNoun = input()
    nouns.append(currentNoun)


for c in adjectives:
    for d in nouns:
        print(c, "as", d)
