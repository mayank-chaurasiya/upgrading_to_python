"""List Uniqueness Checker
Problem: Check if all elements in a list are unique.
If a duplicate is found, exit the loop and print the duplicate.
"""

list1 = [10, 20, 30, 40, 50, 10]
unique_item = set()

for item in list1:
    if item in unique_item:
        print(f"Duplicate item is {item}")
        break
    unique_item.add(item)
