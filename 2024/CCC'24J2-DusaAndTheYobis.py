D = int(input())
firstY = int(input())

if D > firstY:
    D += firstY
    nextY = int(input())

    while D > nextY:
        D += nextY
        nextY = int(input())

        if nextY >= D:
            print(D)
            break
else:
    print(D)
