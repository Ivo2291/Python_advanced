from collections import deque

quantity_of_the_food = int(input())
food_order_quantity = deque(map(int, input().split()))

print(max(food_order_quantity))

while True:
    if not food_order_quantity:
        break

    if food_order_quantity[0] <= quantity_of_the_food:
        quantity_of_the_food -= food_order_quantity[0]
        food_order_quantity.popleft()
    else:
        break

if food_order_quantity:
    food_order_quantity = [str(el) for el in food_order_quantity]
    print(f"Orders left: {' '.join(food_order_quantity)}")
else:
    print("Orders complete")
