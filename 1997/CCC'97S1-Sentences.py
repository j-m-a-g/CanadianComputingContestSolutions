from sys import stdin
n = int(stdin.readline())

subjectList = []
verbList = []
objectList = []

for a in range(n):
    subjects = int(stdin.readline())
    verbs = int(stdin.readline())
    objects = int(stdin.readline())

    for b in range(subjects):
        subjectList.append(stdin.readline().strip("\n"))
    

    for c in range(verbs):
        verbList.append(stdin.readline().strip("\n"))

    
    for d in range(objects):
        objectList.append(stdin.readline().strip("\n"))


for s in subjectList:
    for v in verbList:
        for o in objectList:
            print(s + " " + v + " " + o + ".")
