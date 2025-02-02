from sys import stdin

y = int(stdin.readline()) + 1
yString = str(y)

def findDuplicates():
    global yString
    if yString.count("0") > 1 or yString.count("1") > 1 or yString.count("2") > 1 or yString.count("3") > 1 or yString.count("4") > 1 or yString.count("5") > 1 or yString.count("6") > 1 or yString.count("7") > 1 or yString.count("8") > 1 or yString.count("9") > 1:
        yInt = int(yString)
        yInt += 1
        yString = str(yInt)
        findDuplicates()


findDuplicates()
print(yString)
