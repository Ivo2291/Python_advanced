from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))
toys_dict = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
toys_crafted = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

while materials and magic_level:

    if materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
        continue

    if magic_level[0] == 0:
        magic_level.popleft()
        continue

    elif materials[-1] == 0:
        materials.pop()
        continue

    current_result = materials[-1] * magic_level[0]
    toy_crafted = False

    if current_result < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif current_result > 0:
        for key, value in toys_dict.items():
            if current_result == value:
                toy_crafted = True
                toys_crafted[key] += 1
                materials.pop()
                magic_level.popleft()

        if not toy_crafted:
            magic_level.popleft()
            materials[-1] += 15

if (toys_crafted['Doll'] > 0 and toys_crafted['Wooden train'] > 0) \
        or (toys_crafted['Teddy bear'] > 0 and toys_crafted['Bicycle'] > 0):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for k, v in sorted(toys_crafted.items()):
    if v > 0:
        print(f"{k}: {v}")
