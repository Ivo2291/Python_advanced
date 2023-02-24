from collections import deque


def symbol_check(bee, nec, symbol):
    result = 0
    if symbol == "+":
        result = bee + nec
    elif symbol == "-":
        result = bee - nec
    elif symbol == "*":
        result = bee * nec
    else:
        if nec != 0:
            result = bee / nec

    return abs(result)


bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees[0]
    if current_bee > nectar[-1]:
        nectar.pop()
        continue

    total_honey += symbol_check(bees.popleft(), nectar.pop(), symbols.popleft())

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
