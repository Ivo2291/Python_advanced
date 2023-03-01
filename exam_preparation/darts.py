def points_calc():
    points = 0

    if dartboard[row][col] == "D":
        points += (int(dartboard[row][0]) + int(dartboard[row][SIZE - 1])
                   + int(dartboard[0][col]) + int(dartboard[SIZE - 1][col])) * 2

    elif dartboard[row][col] == "T":
        points += (int(dartboard[row][0]) + int(dartboard[row][SIZE - 1])
                   + int(dartboard[0][col]) + int(dartboard[SIZE - 1][col])) * 3

    else:
        points += int(dartboard[row][col])

    return points


SIZE = 7
dartboard = []

players = input().split(", ")

players_dict = {
                players[0]: {"Turns": 0, "Points": 501},
                players[1]: {"Turns": 0, "Points": 501}
}

for row_index in range(SIZE):
    dartboard.append(input().split())

while True:
    coords = input().strip("()").split(", ")
    row = int(coords[0])
    col = int(coords[1])

    players_dict[players[0]]["Turns"] += 1

    if 0 <= row < SIZE and 0 <= col < SIZE:

        if dartboard[row][col] == "B":
            break

        current_points = points_calc()

        players_dict[players[0]]["Points"] -= current_points

        if players_dict[players[0]]["Points"] <= 0:
            break

        players.reverse()

    else:
        players.reverse()

print(f"{players[0]} won the game with {players_dict[players[0]]['Turns']} throws!")
