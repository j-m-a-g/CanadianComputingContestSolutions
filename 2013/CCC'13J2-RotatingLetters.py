word = list(input())
canBeOnSign = False

for w in word:
    if w in ["I", "O", "S", "H", "Z", "X", "N"]:
        canBeOnSign = True
    else:
        canBeOnSign = False


if canBeOnSign:
    print("YES")
else:
    print("NO")
