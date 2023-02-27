from collections import deque


eggs = deque(map(int, input().split(", ")))
pieces_of_paper = list(map(int, input().split(", ")))
boxes_counter = 0

while eggs and pieces_of_paper:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    elif current_egg == 13:
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue

    else:
        current_paper = pieces_of_paper.pop()

        if current_egg + current_paper <= 50:
            boxes_counter += 1

if boxes_counter > 0:
    print(f"Great! You filled {boxes_counter} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, pieces_of_paper))}")
