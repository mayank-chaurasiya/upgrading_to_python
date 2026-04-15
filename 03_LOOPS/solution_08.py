"""Prime Number Checker
Problem: Check if a number is prime.
"""

input_number = int(input("your number: "))
is_prime = True

if input_number > 1:
    for i in range(2, input_number):
        if (input_number % i) == 0:
            is_prime = False
            break

print(is_prime)
