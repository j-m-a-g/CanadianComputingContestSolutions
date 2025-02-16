from sys import stdin
violations = 0

mustBeInSame = []
x = int(stdin.readline())
for a in range(x):
    mustBeInSame.append(stdin.readline().strip("\n").split())


notInSame = []
y = int(stdin.readline())
for b in range(y):
    notInSame.append(stdin.readline().strip("\n").split())


groups = []
g = int(stdin.readline())
for c in range(g):
    groups.append(stdin.readline().strip("\n").split())


for m in mustBeInSame:
    for g in groups:
        if g.count(m[0]) == 1 and g.count(m[1]) == 0 or g.count(m[0]) == 0 and g.count(m[1]) == 1:
            violations += 1
            break


for n in notInSame:
    for g in groups:
        if g.count(n[0]) == 1 and g.count(n[1]) == 1:
            violations += 1
            break


print(violations)
