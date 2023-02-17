def rectangle(length, width):

    def area():
        return length * width

    def perimeter():
        return (2 * length) + (2 * width)

    if isinstance(length, int) and isinstance(width, int):
        return f"Rectangle area: {area()}" '\n' f"Rectangle perimeter: {perimeter()}"
    else:
        return "Enter valid values!"


print(rectangle('2', 10))
print(rectangle(3, 12))
