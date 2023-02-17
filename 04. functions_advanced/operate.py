import functools


def operate(operator, *args):
    result = 0

    if operator == "+":
        result = functools.reduce(lambda x, y: x + y, args)

    elif operator == "-":
        result = functools.reduce(lambda x, y: x - y, args)

    elif operator == "*":
        result = functools.reduce(lambda x, y: x * y, args)

    elif operator == "/":
        result = functools.reduce(lambda x, y: x / y, args)

    return result


print(operate("+", 1, 2, 3))
