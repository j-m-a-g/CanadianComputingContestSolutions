from sys import stdin

B = int(stdin.readline())
T = int(stdin.readline())
P = int(stdin.readline())

if abs(T - P) >= B:
	print("Y", str(abs(T - P - B)))
else:
	print("N")
