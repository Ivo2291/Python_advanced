numbers = list(map(int, input().split()))
numbers_stack = numbers

reversed_numbers = []

while numbers_stack:
    reversed_numbers.append(numbers_stack.pop())

print(*reversed_numbers)
