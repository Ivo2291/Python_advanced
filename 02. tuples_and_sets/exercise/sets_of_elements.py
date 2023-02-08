first_number, second_number = tuple(map(int, input().split()))

first_set = set()
second_set = set()

for number in range(first_number):
    first_set.add(int(input()))

for number in range(second_number):
    second_set.add(int(input()))

unique_elements = first_set.intersection(second_set)

print(*unique_elements, sep="\n")
