def negative_nums(nums):
    result = sum([num for num in nums if num < 0])
    return result


def positive_nums(nums):
    result = sum([num for num in nums if num > 0])
    return result


def which_are_stronger(positives, negatives):
    if abs(positives) > abs(negatives):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]

print(negative_nums(numbers))
print(positive_nums(numbers))
print(which_are_stronger(positive_nums(numbers), negative_nums(numbers)))
