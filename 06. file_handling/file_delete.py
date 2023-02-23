from os import remove


file = 'numbers.txt'

try:
    remove(file)

except FileNotFoundError:
    print('File already deleted!')
