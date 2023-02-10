rows, columns = [int(num) for num in input().split(', ')]
matrix = []

for row in range(rows):
    matrix.append([int(num) for num in input().split(', ')])

result = 0

for row in range(rows):
    for column in range(columns):
        result += matrix[row][column]

print(result)
print(matrix)
