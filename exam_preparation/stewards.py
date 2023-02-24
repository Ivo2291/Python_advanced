from collections import deque

seats = input().split(", ")
first_sequence = deque(input().split(", "))
second_sequence = deque(input().split(", "))
matched_seats = []
rotations = 0

while len(matched_seats) < 3 and rotations < 10:
    first_digit = first_sequence.popleft()
    second_digit = second_sequence.pop()

    ascii_char = chr(int(first_digit) + int(second_digit))

    first_combination = first_digit + ascii_char
    second_combination = second_digit + ascii_char
    current_seat = ""

    for seat in seats:
        if first_combination == seat:
            current_seat = seat
            break

        elif second_combination == seat:
            current_seat = seat
            break

    if not current_seat:
        first_sequence.append(first_digit)
        second_sequence.appendleft(second_digit)

    else:
        if current_seat not in matched_seats:
            matched_seats.append(current_seat)

    rotations += 1

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
