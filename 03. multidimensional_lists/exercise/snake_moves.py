rows, columns = list(map(int, input().split()))
word = input()

index = 0
matrix = []

for row in range(rows):
    elements = []

    for column in range(columns):
        if index == len(word):
            index = 0

        elements.append(word[index])
        index += 1

    if row % 2 == 0:
        matrix.append(elements)
    else:
        reversed_elements = []

        for el in range(len(elements)):
            reversed_elements.append(elements.pop())
        matrix.append(reversed_elements)

for row in matrix:
    print(''.join(row))
