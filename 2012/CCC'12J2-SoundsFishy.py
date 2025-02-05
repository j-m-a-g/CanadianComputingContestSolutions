reading1 = int(input())
reading2 = int(input())
reading3 = int(input())
reading4 = int(input())

if reading1 < reading2 < reading3 < reading4:
    print("Fish Rising")
elif reading1 > reading2 > reading3 > reading4:
    print("Fish Diving")
elif reading1 == reading2 and reading2 == reading3 and reading3 == reading4:
    print("Fish At Constant Depth")
else:
    print("No Fish")
