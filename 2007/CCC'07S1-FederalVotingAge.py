from sys import stdin

n = int(stdin.readline())
outputs = []
election = [2007, 2, 27]

for a in range(n):
    workingDate = stdin.readline().strip("\n").split()

    if election[0] - int(workingDate[0]) > 18:
        outputs.append("Yes")
    elif election[0] - int(workingDate[0]) == 18:
        if election[1] < int(workingDate[1]):
            outputs.append("No")
        elif election[1] == int(workingDate[1]):
            if election[2] < int(workingDate[2]):
                outputs.append("No")
            else:
                outputs.append("Yes")
        else:
            outputs.append("Yes")
    else:
        outputs.append("No")


for o in outputs:
    print(o)
