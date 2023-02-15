def down_direction(matrix, row_to_check, column_to_check):
    result = 0
    path_matrix = []

    while 0 <= row_to_check + 1 < len(matrix) and matrix[row_to_check + 1][column_to_check] != 'X':
        result += int(matrix[row_to_check + 1][column_to_check])
        path_matrix.append([row_to_check + 1, column_to_check])
        row_to_check += 1

    return result, path_matrix


def up_direction(matrix, row_to_check, column_to_check):
    result = 0
    path_matrix = []

    while 0 <= row_to_check - 1 < len(matrix) and matrix[row_to_check - 1][column_to_check] != 'X':
        result += int(matrix[row_to_check - 1][column_to_check])
        path_matrix.append([row_to_check - 1, column_to_check])
        row_to_check -= 1

    return result, path_matrix


def left_direction(matrix, row_to_check, column_to_check):
    result = 0
    path_matrix = []

    while 0 <= column_to_check - 1 < len(matrix) and matrix[row_to_check][column_to_check - 1] != 'X':
        result += int(matrix[row_to_check][column_to_check - 1])
        path_matrix.append([row_to_check, column_to_check - 1])
        column_to_check -= 1

    return result, path_matrix


def right_direction(matrix, row_to_check, column_to_check):
    result = 0
    path_matrix = []

    while 0 <= column_to_check + 1 < len(matrix) and matrix[row_to_check][column_to_check + 1] != 'X':
        result += int(matrix[row_to_check][column_to_check + 1])
        path_matrix.append([row_to_check, column_to_check + 1])
        column_to_check += 1

    return result, path_matrix


size = int(input())
field = []

for num in range(size):
    field.append(input().split())

bunny_row = 0
bunny_column = 0

for row in range(size):
    for column in range(size):
        if field[row][column] == "B":
            bunny_row = row
            bunny_column = column

best_sum = float("-inf")
best_path = ""
direction = ""

down = down_direction(field, bunny_row, bunny_column)
left = left_direction(field, bunny_row, bunny_column)
up = up_direction(field, bunny_row, bunny_column)
right = right_direction(field, bunny_row, bunny_column)

if down[0] > best_sum and down[1]:
    best_sum = down[0]
    best_path = down[1]
    direction = "down"

if up[0] > best_sum and up[1]:
    best_sum = up[0]
    best_path = up[1]
    direction = "up"

if left[0] > best_sum and left[1]:
    best_sum = left[0]
    best_path = left[1]
    direction = "left"

if right[0] > best_sum and right[1]:
    best_sum = right[0]
    best_path = right[1]
    direction = "right"

print(direction)

for el in best_path:
    print(el)

print(best_sum)
