from sys import stdin

n = int(stdin.readline())
consecutiveDays = []
givenDays = []


def countConsecutive(listObject):
    dayCount = 0
    for z in range(len(listObject)):
        try:
            if listObject[z - 1] == "S" and listObject[z] == "S":
                dayCount += 1
            elif listObject[z] == "S" and listObject[z + 1] == "S" or listObject[z - 1] == "S" and listObject[z] == "S":
                dayCount += 1
            elif listObject[z] == "P" or listObject[z] == "P-" and listObject[z - 1] == "S":
                consecutiveDays.append(dayCount)
                dayCount = 0
        except:
            break

    consecutiveDays.append(dayCount)


for a in range(n):
    workingLine = stdin.readline()
    if workingLine == "\n":
        givenDays.append("")
    else:
        givenDays.append(workingLine.strip("\n"))

if givenDays.count("S") == len(givenDays):
    if len(givenDays) == 1:
        print(0)
    else:
        print(len(givenDays))
else:
    for c in range(len(givenDays)):
        for b in range(len(givenDays)):
            savedIndex = 0
            if givenDays[b] == "P":
                givenDays[b] = "S"
                savedIndex = b
                break

        countConsecutive(givenDays)
        givenDays[savedIndex] = "P-"

        if givenDays.count("P") == 0:
            break

    consecutiveDays.sort(reverse=True)
    if consecutiveDays[0] <= 1:
        print(0)
    else:
        print(consecutiveDays[0])
