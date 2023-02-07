number = int(input())
vip_guests = set()
regular_guests = set()

for guest in range(number):
    reservation_number = input()

    if len(reservation_number) == 8:
        if reservation_number[0].isdigit():
            vip_guests.add(reservation_number)
        else:
            regular_guests.add(reservation_number)

guests_at_the_party = set()
arriving_guests = input()

while arriving_guests != "END":
    guests_at_the_party.add(arriving_guests)

    arriving_guests = input()

all_guests = vip_guests.union(regular_guests)
guests_that_not_came = list(all_guests.difference(guests_at_the_party))

print(len(guests_that_not_came))

sorted_guests = sorted(guests_that_not_came)

for guest in sorted_guests:
    print(guest)
