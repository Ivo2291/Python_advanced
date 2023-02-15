size = int(input())

wonderland = []
alice_position = []
tea_bags_count = 0

directions_dict = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    row_elements = input().split()

    wonderland.append(row_elements)

    for el in row_elements:
        if el == "A":
            alice_position = [row, row_elements.index(el)]
            wonderland[row][alice_position[1]] = "*"

while tea_bags_count < 10:
    movement = input()

    row = alice_position[0] + directions_dict[movement][0]
    column = alice_position[1] + directions_dict[movement][1]

    if 0 <= row < size and 0 <= column < size:

        if wonderland[row][column] == "R":
            wonderland[row][column] = "*"
            break

        alice_position = [row, column]

        if wonderland[row][column].isdigit():
            tea_bags_count += int(wonderland[row][column])

        wonderland[row][column] = "*"

    else:
        break

if tea_bags_count >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in wonderland:
    print(*row)
