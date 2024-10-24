N = int(input())

parking_yesterday = list((input()))
parking_today = list((input()))

print(parking_yesterday)
print(parking_today)

total_parking_yesterday = 0
total_parking_today = 0

"""
for a in parking_yesterday:
    if a == "C":
        total_parking_yesterday = total_parking_yesterday + 1
    print(total_parking_yesterday)
    
for b in parking_yesterday:
    if b == "C":
        total_parking_today = total_parking_today + 1
    print(total_parking_today)
"""


for a in range(N):
    for i in parking_yesterday:
        if i[a] == "C":
            total_parking_yesterday = total_parking_yesterday + 1
        print(total_parking_yesterday)
for b in parking_today:
    print(b)
