from sys import stdin
n = int(stdin.readline())

names = []
bids = []
greatestBid = 0
bidIndex = 0

for a in range(n):
    names.append(stdin.readline().strip("\n"))
    bids.append(int(stdin.readline()))


for b in range(len(bids)):
    try:
        if bids[b + 1] > bids[b]:
            greatestBid = bids[b + 1]
            bidIndex = b + 1
    except:
        break


print(names[bidIndex])
