numOfPlayers = int(input())

points = []
fouls = []
starRatings = []
greaterThan40 = 0

for a in range(numOfPlayers):
    points.append(int(input()))
    fouls.append(int(input()))


for b in range(len(points)):
    starRatings.append(points[b] * 5 - fouls[b] * 3)


for s in starRatings:
    if s > 40:
        greaterThan40 += 1


if greaterThan40 == numOfPlayers:
    print(str(greaterThan40) + "+")
else:
    print(greaterThan40)
