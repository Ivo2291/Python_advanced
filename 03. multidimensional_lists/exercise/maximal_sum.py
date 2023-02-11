import sys

rows, columns = [int(num) for num in input().split()]
matrix = []

for row in range(rows):
    matrix.append([int(num) for num in input().split()])

max_sum = -sys.maxsize
start_row = 0
start_column = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2] +\
                      matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] +\
                      matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2]

        if max_sum < current_sum:
            max_sum = current_sum
            start_row = row
            start_column = column

first_elements = [matrix[start_row][start_column],
                  matrix[start_row][start_column + 1],
                  matrix[start_row][start_column + 2]]

second_elements = [matrix[start_row + 1][start_column],
                   matrix[start_row + 1][start_column + 1],
                   matrix[start_row + 1][start_column + 2]]

third_elements = [matrix[start_row + 2][start_column],
                  matrix[start_row + 2][start_column + 1],
                  matrix[start_row + 2][start_column + 2]]

print(f"Sum = {max_sum}")
print(f"{' '.join(map(str, first_elements))}")
print(f"{' '.join(map(str, second_elements))}")
print(f"{' '.join(map(str, third_elements))}")
