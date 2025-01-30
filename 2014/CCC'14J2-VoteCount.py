numOfVotes = int(input())
votes = list(input())

AVotes, BVotes = 0, 0
for v in votes:
    if v == "A":
        AVotes += 1
    else:
        BVotes += 1

if AVotes > BVotes:
    print("A")
elif AVotes < BVotes:
    print("B")
else:
    print("Tie")
