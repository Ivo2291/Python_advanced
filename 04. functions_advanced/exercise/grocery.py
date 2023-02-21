def grocery_store(**kwargs):
    result = ""
    sorted_store = {key: value for key, value in sorted(kwargs.items(), key=lambda k: (-k[1], -len(k[0]), k[0]))}
    for key, value in sorted_store.items():
        result += f"{key}: {value}" + "\n"

    return result


print(grocery_store(
    apples=1,
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
