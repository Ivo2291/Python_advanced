from collections import deque

command = input()
customers = deque()

while command != "End":

    if command == "Paid":
        print("\n".join(customers))
        customers.clear()

    else:
        current_customer = command
        customers.append(current_customer)

    command = input()

print(f"{len(customers)} people remaining.")
