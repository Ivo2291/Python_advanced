class ValueCannotBeNegative(Exception):
    """"number can not be negative"""


for num in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
