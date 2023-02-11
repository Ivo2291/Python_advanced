size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(num) for num in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
