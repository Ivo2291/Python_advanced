clothes = list(map(int, input().split()))
capacity_of_rack = int(input())
racks = 1

current_capacity = capacity_of_rack

while clothes:
    current_clothes = clothes[-1]
    if current_capacity >= current_clothes:
        current_capacity -= current_clothes
        clothes.pop()
    else:
        racks += 1
        current_capacity = capacity_of_rack

print(racks)
