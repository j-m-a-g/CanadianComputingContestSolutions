from sys import stdin

def findRowSum(listObject):
    currentRowSum = 0
    for l in listObject:
        currentRowSum += int(l)
    
    return currentRowSum


row1 = list(stdin.readline().split())
row2 = list(stdin.readline().split())
row3 = list(stdin.readline().split())
row4 = list(stdin.readline().split())

columnSums = []
rowSums = [findRowSum(row1), findRowSum(row2), findRowSum(row3), findRowSum(row4)]

for a in range(0, len(row1)):
    currentColumnSum = int(row1[a]) + int(row2[a]) + int(row3[a]) + int(row4[a])
    columnSums.append(currentColumnSum)


if rowSums[0] == rowSums[1] and rowSums[0] == rowSums[2] and rowSums[0] == rowSums[3] and rowSums[1] == rowSums[2] and rowSums[1] == rowSums[3] and rowSums[2] == rowSums[3] and columnSums[0] == columnSums[1] and columnSums[0] == columnSums[2] and columnSums[0] == columnSums[3] and columnSums[1] == columnSums[2] and columnSums[1] == columnSums[3] and columnSums[2] == columnSums[3]:
    print("magic")
else:
    print("not magic")
