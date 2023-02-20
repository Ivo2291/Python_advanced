def fill_the_box(height, length, width, *args):
    above_free_space = 0
    free_space = height * length * width

    for el in args:
        if el == "Finish":
            break
        if free_space >= el:
            free_space -= el
        else:
            above_free_space += el - free_space
            free_space = 0

    if free_space:
        return f"There is free space in the box. You could put {free_space} more cubes."
    else:
        return f"No more free space! You have {above_free_space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
