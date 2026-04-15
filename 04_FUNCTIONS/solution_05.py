"""
Write a function that greets a user. If no name is provided,
it should greet with a default name.
"""


def greet_user(name):
    """Function to Greet User"""
    if name:
        print(f"Hello {name}")
    else:
        print("Hello User")


user_str = input("Your Name: ")

greet_user(user_str)
