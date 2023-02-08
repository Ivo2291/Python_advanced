number_of_lines = int(input())

unique_elements = set()

for element in range(number_of_lines):
    current_elements = [el for el in input().split()]

    for el in current_elements:
        unique_elements.add(el)

print(*unique_elements, sep="\n")
