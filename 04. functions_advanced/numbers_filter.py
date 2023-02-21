def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'odd':
            result[key] = [num for num in value if num % 2 != 0]
        elif key == 'even':
            result[key] = [num for num in value if num % 2 == 0]

    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda k: -len(k[1]))}

    return sorted_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
