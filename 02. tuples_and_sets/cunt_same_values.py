numbers = tuple(map(float, input().split()))
unique_numbers = {}

for number in numbers:
    if number not in unique_numbers:
        unique_numbers[number] = numbers.count(number)

for number, occurrence in unique_numbers.items():
    print(f"{number} - {occurrence} times")
