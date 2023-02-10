rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

result = 0

for row in range(rows):
    for column in range(rows):
        if column == row:
            result += matrix[column][row]

print(result)
