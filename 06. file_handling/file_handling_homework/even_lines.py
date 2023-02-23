symbols = ["-", ",", ".", "!", "?"]

file_path = 'text.txt'

with open(file_path, 'r') as text_file:
    lines = text_file.readlines()

for line_number in range(0, len(lines), 2):
    for symbol in symbols:
        lines[line_number] = lines[line_number].replace(symbol, '@')

    splited_line = lines[line_number].split()

    print(*list(reversed(splited_line)))
