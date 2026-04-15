"""Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.
"""

input_str = input("Your string: ")

for char in input_str:
    if input_str.count(char) == 1:
        print(f"Non repeating char is {char}")
        break
