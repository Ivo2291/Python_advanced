from collections import deque

expression = input().split()
numbers = deque()

for element in expression:
    if element not in "+-*/":
        numbers.append(int(element))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()

            if element == "-":
                numbers.appendleft(first_number - second_number)

            elif element == "+":
                numbers.appendleft(first_number + second_number)

            elif element == "*":
                numbers.appendleft(first_number * second_number)

            elif element == "/":
                numbers.appendleft(first_number // second_number)

print(*numbers)
