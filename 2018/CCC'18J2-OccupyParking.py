N = int(input())

parking_yesterday = list((input()))
parking_today = list((input()))

total_parking = 0

for a in range(N):
    if parking_yesterday[a] == "C" and parking_today[a] == "C":
        total_parking = total_parking + 1
        
print(total_parking)
