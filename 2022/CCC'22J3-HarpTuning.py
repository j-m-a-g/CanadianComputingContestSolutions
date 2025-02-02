import re
instruction = list(input())

noteOutput = ""
turnOutput = ""

for i in range(len(instruction)):
    findLetters = re.findall("[A-Z]", instruction[i])
    findNumbers = re.findall("[0-9]", instruction[i])
    if findLetters != [] and findNumbers == []:
        noteOutput += instruction[i]
    else:
        try:
            if instruction[i] == "+":
                print(noteOutput, "tighten", instruction[i + 1])
            elif instruction[i] == "-":
                print(noteOutput, "loosen", instruction[i + 1])
            else:
                noteOutput = ""
        except:
            break
