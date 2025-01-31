previousInstruction = ""
output = []

while True:
    code = input()

    if code != "99999":
        direction = int(code[0]) + int(code[1])

        if direction % 2 == 0 and direction != 0:
            previousInstruction = "right"
            output.append(previousInstruction + " " + code[2] + code[3] + code[4])
        elif direction % 2 != 0:
            previousInstruction = "left"
            output.append(previousInstruction + " " + code[2] + code[3] + code[4])
        else:
            output.append(previousInstruction + " " + code[2] + code[3] + code[4])
    else:
        break

for o in output:
    print(o)
