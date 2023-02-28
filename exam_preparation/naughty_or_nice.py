def naughty_or_nice_list(list_of_kids, *args, **kwargs):
    output = []

    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for command in args:
        number = int(command[0])
        naughty_or_nice = command[2:]
        current_num = 0

        for kid in list_of_kids:
            kid_number = kid[0]
            if number == kid_number:
                current_num += 1

        if current_num == 1:
            for index, element in enumerate(list_of_kids):
                if element[0] == number:
                    kids[naughty_or_nice].append(element[1])
                    list_of_kids.pop(index)
                    break

    for key, value in kwargs.items():
        current_name = 0
        for el in list_of_kids:
            if el[1] == key:
                current_name += 1

        if current_name == 1:
            for idx, kid_name in enumerate(list_of_kids):
                if kid_name[1] == key:
                    kids[value].append(kid_name[1])
                    list_of_kids.pop(idx)

    if list_of_kids:
        for current_kid in list_of_kids:
            kids["Not found"].append(current_kid[1])

    for key, value in kids.items():
        if value:
            output.append(f"{key}: {', '.join(value)}")

    return '\n'.join(output)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
