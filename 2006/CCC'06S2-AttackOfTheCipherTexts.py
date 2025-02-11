from sys import stdin
plaintext = list(stdin.readline().strip("\n"))
cipherText = list(stdin.readline().strip("\n"))
cipherTextLast = list(stdin.readline().strip("\n"))

letters = {
    "A":".", "B":".", "C":".", "D":".", "E":".",
    "F":".", "G":".", "H":".", "I":".", "J":".",
    "K":".", "L":".", "M":".", "N":".", "O":".",
    "P":".", "Q":".", "R":".", "S":".", "T":".",
    "U":".", "V":".", "W":".", "C":".", "X":".",
    "Y":".", "Z":".", " ":"."
}

for a in range(len(plaintext)):
    letters[cipherText[a]] = plaintext[a]


for b in range(len(cipherTextLast)):
    cipherTextLast[b] = letters[cipherTextLast[b]]


for d in cipherTextLast:
    print(d, end="")

print()
