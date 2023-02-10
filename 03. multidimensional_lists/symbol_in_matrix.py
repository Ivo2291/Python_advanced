size = int(input())
matrix = []

for row in range(size):
    matrix.append([el for el in input()])

symbol_to_search = input()
symbol_is_found = False

for row in range(size):
    for column in range(size):
        if symbol_to_search == matrix[row][column]:
            symbol_is_found = True
            print(f"({row}, {column})")
            break

    if symbol_is_found:
        break
else:
    print(f"{symbol_to_search} does not occur in the matrix")
