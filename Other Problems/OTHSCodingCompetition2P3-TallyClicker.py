N = input()
end = "false"
presses = 0

while end == "false":
  if int(N) >= 1111:
    N = int(N) - 1111
    presses = presses + 1
  else:
    end = "true"

print(int(presses) + int(N))
