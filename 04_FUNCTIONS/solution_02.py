"""
Problem: Create a function that takes two numbers as parameters
and returns their sum.
"""

user_num1 = int(input("first Number: "))
user_num2 = int(input("second Number: "))


def sum_of_nums(num1, num2):
    """return the sum of two numbers"""
    return num1 + num2


print(f"Sum of {user_num1} and {user_num2} is {sum_of_nums(user_num1, user_num2)}")
