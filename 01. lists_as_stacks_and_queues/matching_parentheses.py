expression = input()
parentheses_indexes = []

for i in range(len(expression)):

    if expression[i] == "(":
        parentheses_indexes.append(i)

    elif expression[i] == ")":
        start = int(parentheses_indexes.pop())
        end = i + 1
        output = expression[start:end]
        print(output)
