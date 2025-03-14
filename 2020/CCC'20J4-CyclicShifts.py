from sys import stdin
t = stdin.readline().strip("\n")
s = list(stdin.readline().strip("\n"))
shifts = []
shiftsPresent = False

count = 0
while count < len(s) - 1:
    s.append(s[0])
    s.pop(0)
    shifts.append(list(s))
    count += 1


for y in shifts:
    concatenated = ""
    for x in y:
        concatenated += x

    if t.count(concatenated) >= 1:
        shiftsPresent = True


if shiftsPresent == True:
    print("yes")
else:
    print("no")
