"""Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
$8 for children. Everyone gets a $2 discount on Wednesday.
"""

CUSTOMER_AGE = int(input("Enter your age: "))
DAY = "Wednesday"

price = 12 if CUSTOMER_AGE >= 18 else 8

if DAY == "Wednesday":
    price = price - 2

print("Ticket price for you is $", price)
