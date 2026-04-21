"""Write a program to determine if a number is prime"""

user_input = int(input("Enter a number: "))

is_prime = 1

if user_input <= 1:
    is_prime = 0
else:
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            is_prime = 0
            break

if is_prime == 1:
    print(f"{user_input} is a Prime number")
else:
    print(f"{user_input} is not a Prime number")
