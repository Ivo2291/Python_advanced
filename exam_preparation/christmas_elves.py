from collections import deque

elfs_energy = deque(map(int, (input().split())))
materials = deque(map(int, input().split()))

total_energy = 0
toys_crafted = 0
rotations = 0

while elfs_energy and materials:
    current_elf = elfs_energy.popleft()

    if current_elf < 5:
        continue

    material = materials.pop()

    rotations += 1

    needed_energy = material
    eat_cookie = 1
    toys = 1

    if rotations % 3 == 0:
        needed_energy = material * 2
        eat_cookie = 1
        toys = 2

    if rotations % 5 == 0:
        eat_cookie = 0
        toys = 0

    if current_elf >= needed_energy:
        current_elf -= needed_energy
        toys_crafted += toys
        total_energy += needed_energy
        elfs_energy.append(current_elf + eat_cookie)
    else:
        elfs_energy.append(current_elf * 2)
        materials.appendleft(material)

print(f"Toys: {toys_crafted}")
print(f"Energy: {total_energy}")

if elfs_energy:
    print(f"Elves left: {', '.join(map(str, elfs_energy))}")

if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
