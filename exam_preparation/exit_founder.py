players = input().split(", ")

maze_board = []

missed_turns = {"Tom": 0, "Jerry": 0}

for i in range(6):
    maze_board.append(input().split())

while True:
    position = tuple(map(int, input().strip("()").split(", ")))

    if missed_turns[players[0]]:
        missed_turns[players[0]] -= 1
        players.reverse()
        continue

    if maze_board[position[0]][position[1]] == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break

    elif maze_board[position[0]][position[1]] == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    elif maze_board[position[0]][position[1]] == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        missed_turns[players[0]] += 1

    players.reverse()
