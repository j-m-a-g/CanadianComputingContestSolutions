from sys import stdin

n = int(stdin.readline())
auctions = {}

for a in range(n):
    name = stdin.readline().strip("\n")
    amount = int(stdin.readline())
    auctions[name] = amount

amounts = sorted(auctions.values())
for b in auctions:
    if auctions.get(b) == amounts[-1]:
        print(b)
        break
