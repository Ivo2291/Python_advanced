from collections import deque

petrol_pumps = int(input())
stops = deque()

for i in range(petrol_pumps):
    stops.append([int(x) for x in input().split()])

for current_stop in range(petrol_pumps):
    tank = 0

    for petrol, distance in stops:

        tank = tank + petrol - distance

        if tank < 0:
            stops.rotate(-1)
            break
    else:
        print(current_stop)
        break
