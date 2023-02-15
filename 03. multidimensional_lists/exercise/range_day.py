def shooting(some_direction):
    row = my_position[0] + directions[some_direction][0]
    column = my_position[1] + directions[some_direction][1]

    while 0 <= row < size and 0 <= column < size:
        if shooting_field[row][column] == "x":
            shooting_field[row][column] = "."
            return [row, column]

        row += directions[some_direction][0]
        column += directions[some_direction][1]


def move_func(some_direction, steps_to_move):
    row = my_position[0] + (directions[some_direction][0] * steps_to_move)
    column = my_position[1] + (directions[some_direction][1] * steps_to_move)

    if 0 <= row < size and 0 <= column < size and shooting_field[row][column] == ".":
        return [row, column]
    else:
        return my_position


size = 5
shooting_field = []
my_position = []
all_targets_count = 0
shot_targets = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

every_target_is_shot = False

for row_number in range(size):
    symbols = input().split()

    if "A" in symbols:
        my_position = [row_number, symbols.index("A")]

    if "x" in symbols:
        all_targets_count += symbols.count("x")

    shooting_field.append(symbols)

number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split()
    current_command = command[0]
    direction = command[1]

    if current_command == "move":
        steps = int(command[2])

        my_position = move_func(direction, steps)

    elif current_command == "shoot":
        targets_shot = shooting(direction)

        if targets_shot:
            shot_targets.append(targets_shot)

        if all_targets_count == len(shot_targets):
            every_target_is_shot = True
            break


if every_target_is_shot:
    print(f"Training completed! All {all_targets_count} targets hit.")
else:
    print(f"Training not completed! {all_targets_count - len(shot_targets)} targets left.")

for target in shot_targets:
    print(target)
