from sys import stdin

numbers = []

for a in range(4):
    numbers.append(int(stdin.readline()))


numbers.sort()
print(numbers[0])
print(numbers[-1])
