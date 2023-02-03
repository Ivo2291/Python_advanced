from collections import deque

kids = deque(input().split())
tosses = int(input())

while len(kids) > 1:
    for i in range(tosses):
        kids.append(kids.popleft())
        if i == tosses - 1:
            removed_kid = kids.pop()
            print(f"Removed {removed_kid}")

print(f"Last is {''.join(kids)}")
