from sys import stdin
outputs = []

while True:
    currentLine = stdin.readline().strip("\n")

    if currentLine == "CU":
        outputs.append("see you")
    elif currentLine == ":-)":
        outputs.append("I'm happy")
    elif currentLine == ":-(":
        outputs.append("I'm unhappy")
    elif currentLine == ";-)":
        outputs.append("wink")
    elif currentLine == ":-P":
        outputs.append("stick out my tongue")
    elif currentLine == "(~.~)":
        outputs.append("sleepy")
    elif currentLine == "TA":
        outputs.append("totally awesome")
    elif currentLine == "CCC":
        outputs.append("Canadian Computing Competition")
    elif currentLine == "CUZ":
        outputs.append("because")
    elif currentLine == "TY":
        outputs.append("thank-you")
    elif currentLine == "YW":
        outputs.append("you're welcome")
    elif currentLine == "TTYL":
        outputs.append("talk to you later")
        break
    else:
        outputs.append(currentLine)


for o in outputs:
    print(o)
