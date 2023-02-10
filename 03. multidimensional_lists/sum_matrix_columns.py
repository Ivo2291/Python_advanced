rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

for column in range(columns):
    result = 0
    for row in range(rows):
        result += matrix[row][column]

    print(result)
