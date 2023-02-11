def is_in_matrix(row_number, column_number, size_of_matrix):
    return 0 <= row_number < size_of_matrix and 0 <= column_number < size_of_matrix


def cells_around_validation(row, column, given_matrix):
    cells_list = []
    size = len(given_matrix)

    if is_in_matrix(row - 1, column - 1, size) and given_matrix[row - 1][column - 1] > 0:
        cells_list.append([row - 1, column - 1])

    if is_in_matrix(row - 1, column, size) and given_matrix[row - 1][column] > 0:
        cells_list.append([row - 1, column])

    if is_in_matrix(row - 1, column + 1, size) and given_matrix[row - 1][column + 1] > 0:
        cells_list.append([row - 1, column + 1])

    if is_in_matrix(row, column - 1, size) and given_matrix[row][column - 1] > 0:
        cells_list.append([row, column - 1])

    if is_in_matrix(row, column + 1, size) and given_matrix[row][column + 1] > 0:
        cells_list.append([row, column + 1])

    if is_in_matrix(row + 1, column - 1, size) and given_matrix[row + 1][column - 1] > 0:
        cells_list.append([row + 1, column - 1])

    if is_in_matrix(row + 1, column, size) and given_matrix[row + 1][column] > 0:
        cells_list.append([row + 1, column])

    if is_in_matrix(row + 1, column + 1, size) and given_matrix[row + 1][column + 1] > 0:
        cells_list.append([row + 1, column + 1])

    return cells_list


matrix_size = int(input())
matrix = []

for i in range(matrix_size):
    matrix.append(list(map(int, input().split())))

bombs = input().split()

for elements in bombs:
    bomb_row, bomb_column = list(map(int, elements.split(',')))

    if matrix[bomb_row][bomb_column] <= 0:
        continue

    bomb_power = matrix[bomb_row][bomb_column]
    matrix[bomb_row][bomb_column] = 0

    valid_cells = cells_around_validation(bomb_row, bomb_column, matrix)

    for row, column in valid_cells:

        matrix[row][column] -= bomb_power

alive_cells = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")

for row in matrix:
    print(*row)
