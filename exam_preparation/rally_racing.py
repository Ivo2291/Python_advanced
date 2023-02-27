size = int(input())
racing_number = input()

race_route = []

for row_index in range(size):
    race_route.append(input().split())

my_position = [0, 0]
kilometers = 0
finished = False

directions_dict = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

command = input()

while command != "End":

    next_position = [my_position[0] + directions_dict[command][0], my_position[1] + directions_dict[command][1]]

    if race_route[next_position[0]][next_position[1]] == "F":
        kilometers += 10
        finished = True
        race_route[next_position[0]][next_position[1]] = "C"
        break

    if race_route[next_position[0]][next_position[1]] == "T":
        race_route[next_position[0]][next_position[1]] = "."
        kilometers += 30

        for row in range(size):
            for col in range(size):
                if race_route[row][col] == "T":
                    my_position = [row, col]
                    race_route[row][col] = "."

    else:
        my_position = next_position
        kilometers += 10

    command = input()

if not finished:
    race_route[my_position[0]][my_position[1]] = "C"

if finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometers} km.")

for r in race_route:
    print(''.join(r))
