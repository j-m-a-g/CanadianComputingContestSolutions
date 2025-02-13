from sys import stdin

n = int(stdin.readline())
heights = stdin.readline().strip("\n").split()
widths = stdin.readline().strip("\n").split()

areas = []

for a in range(n):
    areas.append(int(widths[a]) * ((int(heights[a]) + int(heights[a + 1])) / 2))


print(sum(areas))
