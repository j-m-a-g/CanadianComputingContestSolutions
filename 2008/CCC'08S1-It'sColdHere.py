from sys import stdin
import re

cities = []
temperatures = []
tempsAsInt = []
coldestCity = ""

while True:
    cityName = stdin.readline().strip("\n")
    cities.append(cityName)
    temperatures.append(cityName.lower().strip(" abcdefghijklmnopqrstuvwxyz"))
    if cityName.lower().count("waterloo") == 1:
        break


for t in temperatures:
    tempsAsInt.append(int(t))


tempsAsInt.sort()

for d in cities:
    if d.count(str(tempsAsInt[0])) == 1:
        coldestCity = d.strip(" -0123456789")


print(coldestCity)
