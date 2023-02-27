def forecast(*args):
    output = []

    data_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for el in args:
        location = el[0]
        weather = el[1]

        if weather == "Sunny":
            data_dict["Sunny"].append(location)

        elif weather == "Cloudy":
            data_dict["Cloudy"].append(location)

        elif weather == "Rainy":
            data_dict["Rainy"].append(location)

    for key, value in data_dict.items():
        if value:
            for current_location in sorted(value):
                output.append(f"{current_location} - {key}")

    return '\n'.join(output)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
