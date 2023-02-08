number_of_lines = int(input())

odd_numbers_set = set()
even_numbers_set = set()

for row in range(1, number_of_lines + 1):
    current_name = input()
    value = 0

    for char in current_name:
        value += ord(char)

    value = value // row

    if value % 2 == 0:
        even_numbers_set.add(int(value))
    else:
        odd_numbers_set.add(int(value))

if sum(odd_numbers_set) == sum(even_numbers_set):
    result = map(str, odd_numbers_set.union(even_numbers_set))

elif sum(odd_numbers_set) > sum(even_numbers_set):
    result = map(str, odd_numbers_set.difference(even_numbers_set))

else:
    result = map(str, odd_numbers_set.symmetric_difference(even_numbers_set))

print(', '.join(result))
