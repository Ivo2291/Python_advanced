rows, columns = [int(num) for num in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())

squares_found = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            squares_found += 1

print(squares_found)
