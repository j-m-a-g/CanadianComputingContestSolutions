from sys import stdin
Pusheen = ["p", "u", "s", "h", "e", "e", "n"]
errors = 0
string = list(stdin.readline().lower().strip("\n"))

for a in range(len(string)):
    if string[a] != Pusheen[a]:
        errors += 1


print(errors)
