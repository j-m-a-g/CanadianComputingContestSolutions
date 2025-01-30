alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
extendedAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

KParam = int(input())
word = input()

wordArray = list(word)
shiftValues = []
indexValues = []

decodedMessage = ""

for w in range(len(wordArray)):
    position = len(wordArray) - (len(wordArray) - (w + 1))
    shiftValues.append(str(3 * position + KParam))


for i in wordArray:
    for a in range(len(alphabet)):
        if alphabet[a] == i:
            indexValues.append(a + 1)


for s in range(len(shiftValues)):
    shift = int(shiftValues[s])
    index = indexValues[s] - 1
    currentPos = 26 + index
    resultPos = currentPos - shift

    decodedMessage += extendedAlphabet[resultPos]


print(decodedMessage)
