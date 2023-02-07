number = int(input())
cars_plate_nums = set()

for car in range(number):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars_plate_nums.add(car_number)
    elif direction == "OUT":
        cars_plate_nums.discard(car_number)

if cars_plate_nums:
    for car_plate in cars_plate_nums:
        print(car_plate)

else:
    print(f"Parking Lot is Empty")
