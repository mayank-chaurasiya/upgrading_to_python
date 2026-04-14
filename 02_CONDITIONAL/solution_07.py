"""Coffee Customization
Problem: Customize a coffee order:
"Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
"""

print("Choose: Small, Medium, or Large")
ORDER_SIZE = input("your order size: ")
EXTRA_SHOT = True

if EXTRA_SHOT:
    COFFEE = ORDER_SIZE + " coffee with an extra shot"
else:
    COFFEE = ORDER_SIZE + " coffee"

print(COFFEE)
