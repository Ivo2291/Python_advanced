def next_position(some_direction, row, column):

    if some_direction == "up":
        return row - 1, column

    elif some_direction == "down":
        return row + 1, column

    elif some_direction == "left":
        return row, column - 1

    elif some_direction == "right":
        return row, column + 1


matrix = []

for i in range(6):
    matrix.append(input().split())

my_position = input()

position_row = int(my_position[1])
position_column = int(my_position[4])

command = input()

while command != "Stop":
    splited_command = command.split(", ")
    current_command = splited_command[0]
    direction = splited_command[1]

    next_row, next_column = next_position(direction, position_row, position_column)

    if current_command == "Create":
        if matrix[next_row][next_column] == ".":
            matrix[next_row][next_column] = splited_command[2]

    elif current_command == "Update":
        if matrix[next_row][next_column] != ".":
            matrix[next_row][next_column] = splited_command[2]

    elif current_command == "Read":
        if matrix[next_row][next_column] != ".":
            print(matrix[next_row][next_column])

    elif current_command == "Delete":
        if matrix[next_row][next_column] != ".":
            matrix[next_row][next_column] = "."

    position_row = next_row
    position_column = next_column

    command = input()

for current_row in matrix:
    print(*current_row)
