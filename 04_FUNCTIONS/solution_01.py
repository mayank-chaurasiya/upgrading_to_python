"""Write a function to calculate and return the square of a number"""

user_num = int(input("Your Number: "))


def square_of_num(number):
    """Return the square of the given number."""
    return number**2


print(f"square of {user_num} is {square_of_num(user_num)}")
