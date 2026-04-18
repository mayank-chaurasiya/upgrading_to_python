"""Recursive Function
Problem: Create a recursive function to calculate the factorial of a number.
"""


def get_factorial(num):
    """Return factorial of the number"""
    if num == 0:
        return 1
    else:
        return num * get_factorial(num - 1)


print(get_factorial(5))
