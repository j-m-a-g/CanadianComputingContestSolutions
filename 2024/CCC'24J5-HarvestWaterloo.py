rows = int(input())
columns = int(input())

rowList = []

for i in range(rows):
    currentRow = input()
    rowList.append(currentRow)


startRow = int(input())
startColumn = int(input())

workingRow = rowList[startRow]

for r in rowList:
    for a in r:
        print(a)
        
    print()

print(rowList)
