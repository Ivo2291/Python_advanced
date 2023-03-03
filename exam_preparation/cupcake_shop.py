from collections import deque


def stock_availability(boxes, command, *args):
    inventory = deque(boxes)

    if command == "delivery":
        inventory.extend(args)

    elif command == "sell":

        if not args:
            inventory.popleft()
        else:
            for el in args:
                if str(el).isdigit():
                    for _ in range(int(el)):
                        inventory.popleft()

                if str(el).isalpha():
                    if el in inventory:
                        while el in inventory:
                            inventory.remove(el)

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
