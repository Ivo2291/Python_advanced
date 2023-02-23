try:
    file = open('numbers.txt', 'r')
    print('File found')

except FileNotFoundError:
    print('File not found')
