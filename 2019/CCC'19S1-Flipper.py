row1 = [1, 2]
row2 = [3, 4]

flips = list(input())

for f in flips:
    if f == "H":
        currentRows = [row1[0], row1[1], row2[0], row2[1]]

        row1[0] = currentRows[2]
        row1[1] = currentRows[3]

        row2[0] = currentRows[0]
        row2[1] = currentRows[1]
    elif f == "V":
        if row1 == [1, 2] or row1 == [3, 4] and row2 == [1, 2] or row2 == [3, 4]:
            row1.sort(reverse = True)
            row2.sort(reverse = True)
        else:
            row1.sort()
            row2.sort()


print(row1[0], row1[1])
print(row2[0], row2[1])
