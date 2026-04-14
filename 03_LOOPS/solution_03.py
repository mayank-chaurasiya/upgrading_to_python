"""Multiplication Table Printer
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
"""

user_input = int(input("Your Number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{user_input} * {i} = {user_input * i}")
