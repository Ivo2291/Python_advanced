from string import punctuation

file_to_read = 'text.txt'
file_to_write = open('line_numbers_output.txt', 'a')

with open(file_to_read, 'r') as file:
    lines = file.readlines()

for line in range(len(lines)):
    chars_count = 0
    punctuation_marks = 0

    for el in lines[line]:
        if el in punctuation:
            punctuation_marks += 1
        elif el.isalpha():
            chars_count += 1

    file_to_write.write(f"Line: {line + 1} {lines[line][:-1]} ({chars_count})({punctuation_marks})\n")

file_to_write.close()
