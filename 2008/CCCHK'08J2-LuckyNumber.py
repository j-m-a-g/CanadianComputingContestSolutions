testCases = int(input())
addedDigits = 0

representations = []
convertedArray = []
digitsToAdd = []

for a in range(testCases):
    currentCase = list(input())
    if len(currentCase) != 1:
        for b in currentCase:
            convertedArray.append(int(b))


        addedDigits = sum(convertedArray) 
        representations.append(addedDigits)
    else:
        for c in currentCase:
            representations.append(int(c))

    addedDigits = 0
    convertedArray = []


for r in representations:
    rList = list(str(r))
    if len(rList) != 1:
        for b in rList:
            convertedArray.append(int(b))

        addedDigits = sum(convertedArray)
        representations.append(addedDigits)
        

    addedDigits = 0
    convertedArray = []


print(representations)
def removeNonSingleDigits():
    blankCount = 0
    for r in range(len(representations)):
        try:
            if len(str(representations[r])) >= 2:
                representations[r] = ""
                blankCount += 1
                

            representations.append(representations[blankCount])
            representations[blankCount] = ""
        except:
            break


removeNonSingleDigits()
print(representations)
for d in representations:
    if d != "":
        print(d)
