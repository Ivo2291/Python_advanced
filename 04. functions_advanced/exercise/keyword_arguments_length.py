def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {"apples": 2, "bananas": 5}

print(kwargs_length(**dictionary))
