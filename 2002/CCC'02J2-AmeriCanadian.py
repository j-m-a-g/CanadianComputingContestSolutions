from sys import stdin
alphabet = list("abcdefghijklmnopqrstuvwxyz")
consonants = list("bcdefghjklmnpqrstvwxz")
outputs = []

while True:
    currentLine = stdin.readline().strip("\n")
    currentLineList = list(currentLine)

    if currentLine != "quit!":
        if len(currentLineList) >= 4:
            for a in range(len(currentLineList)):
                try:
                    if currentLineList[a] in consonants and currentLineList[a + 1] == "o" and currentLineList[a + 2] == "o":
                        outputs.append(currentLineList[0:len(currentLineList)])
                    elif currentLineList[a] in consonants and currentLineList[a + 1] == "o" and currentLineList[-1] == "r":
                        currentLineList.insert(a + 2, "u")
                        outputs.append(currentLineList[0:len(currentLineList)])
                    elif currentLineList[a] in consonants and currentLineList[a + 1] == "o" and currentLineList[a + 2] == "r" and currentLine[-1] in alphabet:
                        outputs.append(currentLineList[0:len(currentLineList)])
                    elif currentLineList[a] in consonants and currentLineList[a + 1] == "o" and currentLineList[a + 2] == "u" and currentLineList[a + 3] == "r":
                        outputs.append(currentLineList[0:len(currentLineList)])
                except:
                    break
        else:
            outputs.append(currentLineList[0:len(currentLineList)])
    else:
        break


for o in outputs:
    resultingWord = "".join(o)
    print(resultingWord)
