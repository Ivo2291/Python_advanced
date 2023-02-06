from collections import deque

cups = deque(map(int, input().split()))
stack_of_bottles = list(map(int, input().split()))
wasted_water = 0

while cups and stack_of_bottles:
    if cups[0] > stack_of_bottles[-1]:
        cups[0] -= stack_of_bottles[-1]

    else:
        wasted_water += stack_of_bottles[-1] - cups[0]
        cups.popleft()

    stack_of_bottles.pop()

if stack_of_bottles:
    print(f"Bottles:", end=' ')
    reversed_stack_of_bottles = []

    for bottle in range(len(stack_of_bottles)):
        reversed_stack_of_bottles.append(stack_of_bottles.pop())

    print(' '.join(map(str, reversed_stack_of_bottles)))

else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
