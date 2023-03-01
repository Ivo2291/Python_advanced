from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while orders and employees:

    if orders[0] <= 0 or orders[0] > 10:
        orders.popleft()
        continue

    current_order = orders.popleft()
    employee = employees.pop()

    if current_order <= employee:
        total_pizzas += current_order

    else:
        current_order -= employee
        total_pizzas += employee
        orders.appendleft(current_order)

if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees))}")

elif orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")
