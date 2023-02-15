number_of_presents = int(input())
size = int(input())

santa_position = ()
neighborhood = []
nice_kids_counter = 0
total_nice_kids = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row_number in range(size):
    elements = input().split()
    neighborhood.append(elements)

    if "S" in elements:
        santa_position = row_number, elements.index("S")
        neighborhood[row_number][santa_position[1]] = "-"

    total_nice_kids += elements.count("V")

command = input()

while command != "Christmas morning":
    santa_position = [santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]]
    current_house = neighborhood[santa_position[0]][santa_position[1]]

    if current_house == "V":
        nice_kids_counter += 1
        number_of_presents -= 1

    elif current_house == "C":
        for direction in directions.values():
            r = santa_position[0] + direction[0]
            c = santa_position[1] + direction[1]

            if neighborhood[r][c].isalpha():
                if neighborhood[r][c] == "V":
                    nice_kids_counter += 1

                number_of_presents -= 1
                neighborhood[r][c] = "-"

                if not number_of_presents:
                    break

    neighborhood[santa_position[0]][santa_position[1]] = "-"

    if not number_of_presents or total_nice_kids == nice_kids_counter:
        break

    command = input()

neighborhood[santa_position[0]][santa_position[1]] = "S"

if not number_of_presents and total_nice_kids > nice_kids_counter:
    print("Santa ran out of presents!")

for row_matrix in neighborhood:
    print(*row_matrix)

if total_nice_kids == nice_kids_counter:
    print(f"Good job, Santa! {nice_kids_counter} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_counter} nice kid/s.")
