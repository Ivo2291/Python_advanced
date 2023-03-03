from math import floor


def movement_check(some_command, r, c):
    path = [r, c]
    if some_command == "up":
        if r < 0:
            path = [size - 1, c]

    elif some_command == "down":
        if r == size:
            path = [0, c]

    elif some_command == "left":
        if c < 0:
            path = [r, size - 1]

    elif some_command == "right":
        if c == size:
            path = [r, 0]

    return path


size = int(input())
matrix = []
my_position = []
my_path = []
total_coins = 0

directions_dict = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row_index in range(size):
    line = input().split()
    if "P" in line:
        my_position = [row_index, line.index("P")]

    matrix.append(line)

my_path.append(my_position)
you_hit_a_wall = False

while total_coins < 100:
    command = input()

    next_row = my_position[0] + directions_dict[command][0]
    next_col = my_position[1] + directions_dict[command][1]

    current_path = movement_check(command, next_row, next_col)
    my_position = [current_path[0], current_path[1]]
    my_path.append(current_path)

    if matrix[my_position[0]][my_position[1]] == "X":
        total_coins /= 2
        you_hit_a_wall = True
        break

    else:
        if matrix[my_position[0]][my_position[1]] != "0" and matrix[my_position[0]][my_position[1]].isdigit():
            total_coins += int(matrix[my_position[0]][my_position[1]])
            matrix[my_position[0]][my_position[1]] = "0"

if you_hit_a_wall:
    print(f"Game over! You've collected {floor(total_coins)} coins.")
else:
    print(f"You won! You've collected {floor(total_coins)} coins.")

print("Your path:")

for i in range(len(my_path)):
    print(my_path[i])
