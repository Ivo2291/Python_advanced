def check_element(row, col):
    if santa_shop[row][col] != "x":

        if santa_shop[row][col] == "G":
            collected_items["Gifts"] += 1

        elif santa_shop[row][col] == "D":
            collected_items["Decorations"] += 1

        elif santa_shop[row][col] == "C":
            collected_items["Cookies"] += 1

        santa_shop[row][col] = "x"


def direction(some_direction, row, col, some_steps):
    for _ in range(some_steps):
        if decorations == collected_items["Decorations"]\
                and cookies == collected_items["Cookies"]\
                and gifts == collected_items["Gifts"]:

            return [row, col]

        if some_direction == "up":
            row -= 1
            if row < 0:
                row = rows - 1

        elif some_direction == "down":
            row += 1
            if row == rows:
                row = 0

        elif some_direction == "left":
            col -= 1
            if col < 0:
                col = cols - 1

        elif some_direction == "right":
            col += 1
            if col == cols:
                col = 0

        check_element(row, col)

    return [row, col]


rows, cols = [int(x) for x in input().split(', ')]

santa_shop = []
santa_row = 0
santa_column = 0
gifts = 0
decorations = 0
cookies = 0

collected_items = {
    "Gifts": 0,
    "Decorations": 0,
    "Cookies": 0
}

for row_index in range(rows):
    line = input().split()
    if "Y" in line:
        santa_row = row_index
        santa_column = line.index("Y")
        line[santa_column] = "x"
    if "D" in line:
        decorations += line.count("D")
    if "C" in line:
        cookies += line.count("C")
    if "G" in line:
        gifts += line.count("G")

    santa_shop.append(line)

command = input()

while command != "End":
    splited_command = command.split('-')
    current_direction = splited_command[0]
    steps = int(splited_command[1])

    santa_row, santa_column = direction(current_direction, santa_row, santa_column, steps)

    if decorations == collected_items["Decorations"] \
            and cookies == collected_items["Cookies"] \
            and gifts == collected_items["Gifts"]:

        print("Merry Christmas!")
        break

    command = input()

santa_shop[santa_row][santa_column] = "Y"

print("You've collected:")

print(f"- {collected_items['Decorations']} Christmas decorations")
print(f"- {collected_items['Gifts']} Gifts")
print(f"- {collected_items['Cookies']} Cookies")

for field_row in santa_shop:
    print(*field_row)
