"""Factorial Calculator
Problem: Compute the factorial of a number using a while loop.
"""

input_number = int(input("Your number: "))
n = input_number
factorial = 1

while input_number > 1:
    factorial *= input_number
    input_number -= 1

print(f"Factorial of {n} is {factorial}")
