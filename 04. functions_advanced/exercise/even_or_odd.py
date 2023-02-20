def even_odd(*args):
    if args[-1] == "odd":
        return [num for num in args if isinstance(num, int) and num % 2 != 0]
    else:
        return [num for num in args if isinstance(num, int) and num % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
