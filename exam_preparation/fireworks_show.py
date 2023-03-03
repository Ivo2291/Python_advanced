from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]

fireworks_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

you_made_it = False

while firework_effects and explosive_power:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    firework = firework_effects.popleft()
    explosive = explosive_power.pop()
    result = firework + explosive

    if result % 3 == 0 and result % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1

    elif result % 3 == 0:
        fireworks_dict["Palm Fireworks"] += 1

    elif result % 5 == 0:
        fireworks_dict["Willow Fireworks"] += 1

    else:
        firework -= 1
        firework_effects.append(firework)
        explosive_power.append(explosive)

    if fireworks_dict["Palm Fireworks"] >= 3 and \
            fireworks_dict["Willow Fireworks"] >= 3 and \
            fireworks_dict["Crossette Fireworks"] >= 3:

        you_made_it = True
        break

if you_made_it:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for key, value in fireworks_dict.items():
    print(f"{key}: {value}")
