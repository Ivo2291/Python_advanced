SIZE = 6

board = []
total_points = 0
throws = 3
throws_coords = []

for _ in range(SIZE):
    board.append(input().split())

for throw in range(throws):
    current_coords = input().strip("()").split(", ")

    if current_coords in throws_coords:
        continue

    throws_coords.append(current_coords)
    row_index = int(current_coords[0])
    col_index = int(current_coords[1])

    if 0 <= row_index < SIZE and 0 <= col_index < SIZE:

        if board[row_index][col_index] == "B":
            for row in range(SIZE):
                if board[row][col_index].isdigit():
                    total_points += int(board[row][col_index])

if total_points < 100:
    difference = 100 - total_points
    print(f"Sorry! You need {difference} points more to win a prize.")

elif total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")

elif total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")

else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
