from sys import stdin
t = int(stdin.readline())
outputs = []

abc = list("ABC")
d_e_f = list("DEF")
ghi = list("GHI")
jkl = list("JKL")
mno = list("MNO")
pqrs = list("PQRS")
tuv = list("TUV")
wxyz = list("WXYZ")

for a in range(t):
    currentLine = stdin.readline().strip("\n").split("-")
    currentLineList = []

    for c in currentLine:
        for d in c:
            currentLineList.append(d)

    for e in range(len(currentLineList)):
        if currentLineList[e] in abc:
            currentLineList[e] = "2"
        elif currentLineList[e] in d_e_f:
            currentLineList[e] = "3"
        elif currentLineList[e] in ghi:
            currentLineList[e] = "4"
        elif currentLineList[e] in jkl:
            currentLineList[e] = "5"
        elif currentLineList[e] in mno:
            currentLineList[e] = "6"
        elif currentLineList[e] in pqrs:
            currentLineList[e] = "7"
        elif currentLineList[e] in tuv:
            currentLineList[e] = "8"
        elif currentLineList[e] in wxyz:
            currentLineList[e] = "9"

    for f in range(len(currentLineList)):
        if f == 3 or f == 7:
            currentLineList.insert(f, "-")

    outputs.append(currentLineList)


for o in outputs:
    for p in range(len(o)):
        print(o[0] + o[1] + o[2] + o[3] + o[4] + o[5] + o[6] + o[7] + o[8] + o[9] + o[10] + o[11])
        break
