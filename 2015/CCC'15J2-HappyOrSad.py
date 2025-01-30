message = input()

if message.count(":-)") > message.count(":-("):
    print("happy")
elif message.count(":-)") < message.count(":-("):
    print("sad")
elif message.count(":-)") == message.count(":-(") and message.count(":-)") != 0 and message.count(":-(") != 0:
    print("unsure")
else:
    print("none")
