number = int(input())
stack = []

for num in range(number):
    queries = input().split()

    if queries[0] == "1":
        current_number = int(queries[1])
        stack.append(current_number)

    if stack:
        if queries[0] == "2":
            stack.pop()

        elif queries[0] == "3":
            print(max(stack))

        elif queries[0] == "4":
            print(min(stack))

reversed_stack = []

for el in range(len(stack)):
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))
