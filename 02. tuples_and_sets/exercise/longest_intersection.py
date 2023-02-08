number_of_lines = int(input())

longest_intersection = set()

for number in range(number_of_lines):
    ranges = input().split("-")
    first_range_start, first_range_end = map(int, ranges[0].split(","))
    second_range_start, second_range_end = map(int, ranges[1].split(","))
    first_set = {num for num in range(first_range_start, first_range_end + 1)}
    second_set = {num for num in range(second_range_start, second_range_end + 1)}

    if len(first_set.intersection(second_set)) > len(longest_intersection):
        longest_intersection = first_set.intersection(second_set)

result = list(map(str, longest_intersection))

print(f"Longest intersection is [{', '.join(result)}] with length {len(longest_intersection)}")
