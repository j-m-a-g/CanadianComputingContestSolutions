N = int(input())

person_availability_list = []

for i in range(N):
    person_availability = input()
    person_availability_single = list(person_availability)
    print(person_availability_single)
    person_availability_list.extend(person_availability_single)


print(person_availability_list)

index_as_N = N - 1
N_index_factor = index_as_N * 5

for i in range(len(person_availability_list)):
    print(i)
    if person_availability_list[i] == "Y" and person_availability_list[i + N_index_factor] == "Y":
        print("Something")
