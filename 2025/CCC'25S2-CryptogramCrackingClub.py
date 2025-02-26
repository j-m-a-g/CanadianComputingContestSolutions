from sys import stdin
import math

s = list(stdin.readline().strip("\n"))
c = int(stdin.readline())

numbers = list("0123456789")
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

expandedString = []
totalExpand = []
concatenated = ""
concatenatedString = ""

for a in range(len(s)):
    if a < len(s) - 1:
        if s[a] in numbers:
            concatenated += s[a]
        elif s[a] in lowercase or s[a] in uppercase:
            concatenatedString += s[a]

        if s[a] in numbers and s[a + 1] in lowercase or s[a + 1] in uppercase:
            try:
                for b in range(int(concatenated)):
                    expandedString.append(concatenatedString)
            except:
                pass

            concatenated = ""
            concatenatedString = ""
    elif a == len(s) - 1:
        if s[a] in numbers:
            concatenated += s[a]
        
        try:
            for b in range(int(concatenated)):
                expandedString.append(concatenatedString)
        except:
            pass


factor = math.ceil(c / len(expandedString))
for b in range(factor + 1):
    totalExpand.extend(expandedString)


print(totalExpand)
print(totalExpand[c])
