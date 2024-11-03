N = int(input())

N_added = N + 1

N_str = str(N_added)

N_list = list(N_str)

"""
while str(N_str).find("0") == True:
    N_added = N_added + 1
    print(N_added)
    while str(N_str).find("0") == True:
        N_added = N_added + 1
        print(N_added)
        
"""


N_list_length = len(N_list) - 1
print(N_list_length)

for i in range(N_list_length):
    print(N_added)
    while N_list[i] == "0":
        N_added = N_added + 1
        N_list.pop(i)
        break

print(N_added)
