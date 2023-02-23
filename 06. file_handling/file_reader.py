file = open('./numbers.txt', 'r')

result = sum([int(num) for num in file])

print(result)
