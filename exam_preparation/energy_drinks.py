from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

stamat_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    drink = energy_drinks.popleft()

    result = current_caffeine * drink

    if result + stamat_caffeine <= 300:
        stamat_caffeine += result

    else:
        energy_drinks.append(drink)
        if stamat_caffeine - 30 >= 0:
            stamat_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
