def knight_attacks_func(board, row_to_check, column_to_check):
    result = 0
    moves = [
        [row_to_check + 2, column_to_check - 1],
        [row_to_check + 2, column_to_check + 1],
        [row_to_check + 1, column_to_check - 2],
        [row_to_check + 1, column_to_check + 2],
        [row_to_check - 2, column_to_check - 1],
        [row_to_check - 2, column_to_check + 1],
        [row_to_check - 1, column_to_check - 2],
        [row_to_check - 1, column_to_check + 2]
    ]

    for current_row, current_column in moves:
        if 0 <= current_row < len(board) and 0 <= current_column < len(board) \
                and board[current_row][current_column] == "K":
            result += 1

    return result


size = int(input())
chess_board = []

for num in range(size):
    chess_board.append(list(input()))

removed_knights = 0

while True:
    attacks_counter = 0
    knight_row = 0
    knight_column = 0

    for row in range(size):
        for column in range(size):
            if chess_board[row][column] == "K":
                counter = knight_attacks_func(chess_board, row, column)

                if counter > attacks_counter:
                    attacks_counter = counter
                    knight_row = row
                    knight_column = column

    if attacks_counter == 0:
        break

    chess_board[knight_row][knight_column] = "0"
    removed_knights += 1

print(removed_knights)
