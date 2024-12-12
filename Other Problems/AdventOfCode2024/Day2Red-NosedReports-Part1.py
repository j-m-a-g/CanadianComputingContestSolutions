workingFile = "Other Problems\\AdventOfCode2024\\plantNuclearReports.txt"

plantNuclearReports = open(workingFile, "r")

loopRange = 0

with plantNuclearReports as lines:
    loopRange = len(lines.readlines())
    

plantNuclearReports = open(workingFile, "r")

nuclearReportsList = []
singleReadLineList = []

unsafeReports = 0

for i in range(loopRange):
    singleReadLine = plantNuclearReports.readline().replace("\n", "")
    #singleReadLine = plantNuclearReports.readline().replace(" ", "")
    singleReadLineList = list(singleReadLine)
    for a in range(len(singleReadLineList)):
        if singleReadLineList[a] == " ":
            singleReadLineList[a] = singleReadLineList[a - 1] + singleReadLineList[a]
    
    #singleReadLineList = list(singleReadLine)
    # for a in range(len(singleReadLineList)):
    #     increaseOrDecrease = abs(singleReadLineList[a] - singleReadLineList[a + 1])
    #     if (increaseOrDecrease > 3):
    #         unsafeReports += 1
    
    # nuclearReportsList.append(list(singleReadLine))


print(singleReadLineList)
