from sys import stdin
bad = 0

n = int(stdin.readline())
names1 = stdin.readline().strip("\n").split()
names2 = stdin.readline().strip("\n").split()

if n % 2 != 0:
    print("bad")
else:
    partners = []

    for a in range(len(names1)):
        currentPartners = [names1[a], names2[a]]
        partners.append(currentPartners)


    for p in partners:
        p.sort()


    partners.sort()

    for c in range(len(partners)):
        try:
            if partners[c][0] == partners[c + 1][0] and partners[c][1] != partners[c + 1][1]:
                bad += 1
            elif partners[c][0] == partners[c][1]:
                bad += 1
        except:
            break


    if bad > 0:
        print("bad")
    else:
        print("good")
