from collections import deque

amount_of_water = int(input())
people = deque()
command = input()

while command != "Start":
    current_person = command
    people.append(current_person)

    command = input()

second_command = input()

while second_command != "End":

    if "refill" in second_command:
        split_command = second_command.split()
        liters = int(split_command[1])

        amount_of_water += liters

    else:
        liters = int(second_command)
        person_name = people.popleft()

        if liters > amount_of_water:
            print(f"{person_name} must wait")
        else:
            amount_of_water -= liters
            print(f"{person_name} got water")

    second_command = input()

print(f"{amount_of_water} liters left")
