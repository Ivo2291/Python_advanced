from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    result = []

    while numbers:
        kwargs['a'] += numbers.popleft()
        if not numbers:
            break

        kwargs['s'] -= numbers.popleft()
        if not numbers:
            break

        if numbers[0] != 0:
            kwargs['d'] /= numbers.popleft()
        else:
            numbers.popleft()

        if not numbers:
            break

        kwargs['m'] *= numbers.popleft()

    sorted_dict = {k: v for k, v in sorted(kwargs.items(), key=lambda k: (-k[1], k[0]))}

    for key, value in sorted_dict.items():
        result.append(f"{key}: {value:.1f}")

    return '\n'.join(result)


print(math_operations(6.0, a=0, s=0, d=5, m=0))
