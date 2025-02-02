N = int(input())
k = int(input())
sums = []

for a in range(k + 1):
    sums.append(N * 10 ** a)


print(sum(sums))
