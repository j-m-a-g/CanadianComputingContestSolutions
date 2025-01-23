keysPressed = list(input())
display = list(input())

print(keysPressed)
print(display)

pressedKey = ""
sillyKey = ""
quietKey = ""

if len(keysPressed) == len(display):
    for i in range(len(keysPressed)):
        if display[i] != keysPressed[i]:
            pressedKey = keysPressed[i]
            sillyKey = display[i]
            quietKey = "-"
else:
    keysSorted = sorted(keysPressed)
    displaySorted = sorted(display)

    print(keysSorted)
    print(displaySorted)

    for h in range(len(displaySorted)):
        if keysSorted[h] != displaySorted[h]:
            quietKey = keysSorted[h]
            break

    pressedKey = keysSorted[-1]
    sillyKey = displaySorted[-1]


print(pressedKey, sillyKey)
print(quietKey)
