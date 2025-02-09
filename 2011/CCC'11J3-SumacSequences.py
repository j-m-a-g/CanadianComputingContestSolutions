from sys import stdin

t1 = int(stdin.readline())
t2 = int(stdin.readline())

sequence = [t1, t2]
sequence.append(t1 - t2)

while sequence[-1] <= sequence[-2]:
    sequence.append(sequence[-2] - sequence[-1])


print(len(sequence))
