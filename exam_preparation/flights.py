def flights(*flights_info):
    flights_dict = {}

    for i in range(0, len(flights_info), 2):
        if flights_info[i] == "Finish":
            return flights_dict

        destination = flights_info[i]
        passengers = flights_info[i + 1]

        if destination not in flights_dict:
            flights_dict[destination] = 0

        flights_dict[destination] += passengers

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
