from collections import deque


def next_position(direction, row, column):
    if direction == "up":
        return row - 1, column

    elif direction == "down":
        return row + 1, column

    elif direction == "left":
        return row, column - 1

    elif direction == "right":
        return row, column + 1


SIZE = 6
matrix = []
rover_row = 0
rover_col = 0
deposits = {"W": 0, "M": 0, "C": 0}

for i in range(SIZE):
    line = input().split()

    if "E" in line:
        rover_row = i
        rover_col = line.index("E")

    matrix.append(line)

commands = deque(input().split(", "))

while commands:
    current_command = commands.popleft()

    rover_next_position = next_position(current_command, rover_row, rover_col)
    rover_row = rover_next_position[0]
    rover_col = rover_next_position[1]

    if rover_next_position[0] == SIZE:
        rover_row = 0

    if rover_next_position[0] < 0:
        rover_row = SIZE - 1

    if rover_next_position[1] == SIZE:
        rover_col = 0

    if rover_next_position[1] < 0:
        rover_col = SIZE - 1

    if matrix[rover_row][rover_col] == "W":
        deposits["W"] += 1
        print(f"Water deposit found at {rover_row, rover_col}")

    elif matrix[rover_row][rover_col] == "M":
        deposits["M"] += 1
        print(f"Metal deposit found at {rover_row, rover_col}")

    elif matrix[rover_row][rover_col] == "C":
        deposits["C"] += 1
        print(f"Concrete deposit found at {rover_row, rover_col}")

    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at {rover_row, rover_col}")
        break

    matrix[rover_row][rover_col] = "-"

if deposits["W"] > 0 and deposits["C"] > 0 and deposits["M"] > 0:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
