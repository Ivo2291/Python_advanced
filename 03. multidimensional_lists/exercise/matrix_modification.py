size = int(input())
matrix = []

for rows in range(size):
    matrix.append([int(num) for num in input().split()])

command = input()

while command != "END":
    split_command = command.split()
    current_command = split_command[0]
    row, column, value = [int(num) for num in split_command[1:]]

    if 0 <= row < size and 0 <= column < size:

        if current_command == "Add":
            matrix[row][column] += value

        elif current_command == "Subtract":
            matrix[row][column] -= value

    else:
        print("Invalid coordinates")

    command = input()

for row in matrix:
    print(*row)
