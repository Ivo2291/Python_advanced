from collections import deque

chocolates = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
milkshakes_count = 0
enough_milkshakes = False

while cups_of_milk and chocolates:
    invalid_ingredient = False

    if chocolates[-1] <= 0:
        chocolates.pop()
        invalid_ingredient = True

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        invalid_ingredient = True

    if invalid_ingredient:
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshakes_count += 1
        chocolates.pop()
        cups_of_milk.popleft()

        if milkshakes_count == 5:
            enough_milkshakes = True
            break
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if enough_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")
