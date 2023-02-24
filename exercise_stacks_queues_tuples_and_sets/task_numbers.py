first_sequence, second_sequence = set(map(int, input().split())), set(map(int, input().split()))

number_of_lines = int(input())

for num in range(number_of_lines):
    command = input().split()
    current_command = ' '.join(command[:2])
    numbers_set = {int(el) for el in command[2:]}

    if current_command == "Add First":
        first_sequence = first_sequence.union(numbers_set)

    elif current_command == "Add Second":
        second_sequence = second_sequence.union(numbers_set)

    elif current_command == "Remove First":
        for number in numbers_set:
            if number in first_sequence:
                first_sequence.remove(number)

    elif current_command == "Remove Second":
        for number in numbers_set:
            if number in second_sequence:
                second_sequence.remove(number)

    elif current_command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(', '.join(map(str, first_sequence)))
print(', '.join(map(str, second_sequence)))
