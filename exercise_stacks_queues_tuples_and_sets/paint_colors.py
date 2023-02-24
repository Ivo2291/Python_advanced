from collections import deque


def odd_even_length(some_string):
    result = 0

    if len(some_string) % 2 == 0:
        result += len(some_string) // 2
    else:
        result += len(some_string) // 2 + 1

    return result


string = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
found_colors = []

while string:

    if len(string) == 1:
        first_substring = string.pop()
        second_substring = ''
    else:
        first_substring = string.popleft()
        second_substring = string.pop()

    combination_one = first_substring + second_substring
    combination_two = second_substring + first_substring

    if combination_one in main_colors:
        found_colors.append(combination_one)

    elif combination_two in main_colors:
        found_colors.append(combination_two)

    elif combination_one in secondary_colors:
        found_colors.append(combination_one)

    elif combination_two in secondary_colors:
        found_colors.append(combination_two)

    else:
        first_substring = first_substring[0:-1]
        second_substring = second_substring[0:-1]
        index_to_add = odd_even_length(string)

        if first_substring:
            string.insert(index_to_add, first_substring)

        if second_substring:
            string.insert(index_to_add, second_substring)

combinations = {"orange": ["red", "yellow"],
                "purple": ["red", "blue"],
                "green": ["yellow", "blue"]
                }

colors_output = []

for color in found_colors:
    if color in main_colors:
        colors_output.append(color)

    elif color in secondary_colors:
        for key, value in combinations.items():
            if key == color:
                needed_colors = all([el in found_colors for el in value])

                if needed_colors:
                    colors_output.append(key)

print(colors_output)
