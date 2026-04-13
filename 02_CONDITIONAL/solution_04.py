"""Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
"""

import sys

FRUIT_NAME = input("Fruit name? : ")
if FRUIT_NAME != "Banana":
    print("No data available for the selected fruit")
    sys.exit()


FRUIT_CURRENT_COLOR = input("Current color of food? : ")
if FRUIT_CURRENT_COLOR == "Green":
    print("Unripe")
elif FRUIT_CURRENT_COLOR == "Yellow":
    print("Ripe")
elif FRUIT_CURRENT_COLOR == "Brown":
    print("OverRipe")
else:
    print("Can't understand")
