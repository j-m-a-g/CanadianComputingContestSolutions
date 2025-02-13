from sys import stdin
dict = {}
scores = []
names = []
outputs = []

n = int(stdin.readline())

for a in range(n):
    currentComputer = stdin.readline().strip("\n").split()
    score = (2 * int(currentComputer[1])) + (3 * int(currentComputer[2])) + int(currentComputer[3])
    
    dict[currentComputer[0]] = score
    scores.append(score)
    names.append(currentComputer[0])
    

scores.sort(reverse=True)

for b in range(len(names)):
    if dict[names[b]] == scores[0] or dict[names[b]] == scores[1]:
        outputs.append(names[b])


outputs.sort()
if len(outputs) >= 3:
    print(outputs[0])
    print(outputs[1])
else:
    for o in outputs:
        print(o)
