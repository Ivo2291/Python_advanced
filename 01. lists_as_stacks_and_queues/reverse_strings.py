string = list(input())
reversed_stack = []

while string:
    reversed_stack.append(string.pop())

print("".join(reversed_stack))
