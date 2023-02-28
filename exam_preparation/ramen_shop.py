from collections import deque

bowls_of_ramen = list(map(int, input().split(", ")))
costumers = deque(map(int, input().split(", ")))
we_served_all_the_costumers = False

while True:
    if not costumers:
        we_served_all_the_costumers = True
        break

    if not bowls_of_ramen:
        break

    bowl = bowls_of_ramen.pop()
    current_costumer = costumers.popleft()

    if bowl == current_costumer:
        continue

    elif bowl > current_costumer:
        bowl -= current_costumer
        bowls_of_ramen.append(bowl)

    else:
        current_costumer -= bowl
        costumers.appendleft(current_costumer)

if we_served_all_the_costumers:
    print("Great job! You served all the customers.")

    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, costumers))}")
