rows, columns = [int(num) for num in input().split()]

first_letter = ord('a')
matrix = []

for row in range(rows):
    part_of_matrix = []
    for column in range(columns):
        part_of_matrix.append(chr(first_letter + row) + chr(first_letter + column + row) + chr(first_letter + row))

    matrix.append(part_of_matrix)

for row in matrix:
    print(*row)
