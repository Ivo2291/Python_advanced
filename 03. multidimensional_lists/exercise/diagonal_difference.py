size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(num) for num in input().split()])

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)
