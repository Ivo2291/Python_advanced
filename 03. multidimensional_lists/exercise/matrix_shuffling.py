def is_valid(row_to_check, column_to_check, rows_size, columns_size):
    if 0 <= row_to_check < rows_size and 0 <= column_to_check < columns_size:
        return True


rows, columns = [int(num) for num in input().split()]
matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

command = input()

while command != "END":
    split_command = command.split()

    if len(split_command) != 5 or split_command[0] != "swap":
        print("Invalid input!")
    else:
        row1, column1, row2, column2 = [int(num) for num in split_command[1:]]

        if is_valid(row1, column1, rows, columns) and is_valid(row2, column2, rows, columns):
            matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]

            for row in matrix:
                print(' '.join(row))

        else:
            print("Invalid input!")

    command = input()
