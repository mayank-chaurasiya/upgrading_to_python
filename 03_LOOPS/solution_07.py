"""Validate Input
Problem: Keep asking the user for input until they enter a number between 1 and 10.
"""

while True:
    input_num = int(input("Your Number b/w 1 and 10: "))
    if 1 <= input_num <= 10:
        print("Thanks")
        break
