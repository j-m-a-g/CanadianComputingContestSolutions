from sys import stdin
outputs = []

n = int(stdin.readline())
boxes = {}
for a in range(n):
    currentBox = stdin.readline().strip("\n").split()
    currentVolume = int(currentBox[0]) * int(currentBox[1]) * int(currentBox[2])
    currentSum = int(currentBox[0]) + int(currentBox[1]) + int(currentBox[2])
    boxes[currentSum] = currentVolume


m = int(stdin.readline())
packages = {}
for b in range(m):
    currentPackage = stdin.readline().strip("\n").split()
    currentPackageVolume = int(currentPackage[0]) * int(currentPackage[1]) * int(currentPackage[2])
    currentPackageSum = int(currentPackage[0]) + int(currentPackage[1]) + int(currentPackage[2])
    packages[currentPackageSum] = currentPackageVolume


for p in packages:
    foundMatch = False
    for b in sorted(boxes):
        if p <= b and packages.get(p) <= boxes.get(b):
            outputs.append(boxes.get(b))
            foundMatch = True
            break


    if foundMatch == False:
        outputs.append("Item does not fit.")


for o in outputs:
    print(o)
