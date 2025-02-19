from sys import stdin

swaps = 0
books = list(stdin.readline().strip("\n"))
booksSorted = []
for b in books:
    booksSorted.append(b)

booksSorted.sort()


def booksFunction(listObject):
    global swaps
    for a in range(len(listObject)):
        if listObject[a] == "M":
            try:
                if listObject[a + 1] == "L":
                    listObject[a] = "L"
                    listObject[a + 1] = "M"
                    swaps += 1
            except:
                break
        elif listObject[a] == "S":
            try:
                if listObject[a + 1] == "L":
                    listObject[a] = "L"
                    listObject[a + 1] = "S"
                    swaps += 1
                elif listObject[a + 1] == "M":
                    listObject[a] = "M"
                    listObject[a + 1] = "S"
                    swaps += 1
            except:
                break

    if listObject != booksSorted:
        booksFunction(listObject)


booksFunction(books)
print(swaps)
