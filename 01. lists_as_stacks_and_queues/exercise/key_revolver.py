from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
stack_of_bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_intelligence = int(input())
count_of_bullets = 0
total_bullets = 0

while stack_of_bullets and locks:
    if stack_of_bullets[-1] <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    stack_of_bullets.pop()
    count_of_bullets += 1
    total_bullets += 1

    if count_of_bullets == size_of_barrel:
        if stack_of_bullets:
            print("Reloading!")
            count_of_bullets = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    bullets_cost = bullet_price * total_bullets
    money_earned = value_of_intelligence - bullets_cost
    print(f"{len(stack_of_bullets)} bullets left. Earned ${money_earned}")
