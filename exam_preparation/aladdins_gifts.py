from collections import deque


def result_check(first_num, second_num):
    res = 0
    if first_num + second_num < 100:
        if (first_num + second_num) % 2 == 0:
            first_num *= 2
            second_num *= 3
        else:
            first_num *= 2
            second_num *= 2

        res += first_num + second_num

    elif first_num + second_num > 499:
        res += (first_num + second_num) / 2

    else:
        res += first_num + second_num

    return res


materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    result = result_check(material, magic)

    if 100 <= result <= 199:
        gifts["Gemstone"] += 1

    elif 200 <= result <= 299:
        gifts["Porcelain Sculpture"] += 1

    elif 300 <= result <= 399:
        gifts["Gold"] += 1

    elif 400 <= result <= 499:
        gifts["Diamond Jewellery"] += 1

if gifts["Gemstone"] and gifts["Porcelain Sculpture"] or gifts["Diamond Jewellery"] and gifts["Gold"]:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(gifts.items()):
    if value > 0:
        print(f"{key}: {value}")
