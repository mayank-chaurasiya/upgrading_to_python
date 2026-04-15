"""
Write a function that greets a user. If no name is provided,
it should greet with a default name.
"""


def greet_user(name="User"):
    """Function to Greet User"""
    return "Hello, " + name + "!"


print(greet_user("Mayank"))
