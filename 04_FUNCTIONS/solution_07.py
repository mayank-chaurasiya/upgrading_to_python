"""
Problem:
Write a function that takes variable number of arguments and returns their sum.
"""


def sum_all(*args):
    """return sum of all the inputs"""
    return sum(args)


print(sum_all(1, 2))
print(sum_all(1, 2, 6, 5, 43))
