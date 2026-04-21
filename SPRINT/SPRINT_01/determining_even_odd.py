"""Write a program to check whether a number is even or odd."""

user_input = int(input("Enter a number: "))

if user_input > 0:

    if user_input % 2 == 0:
        print(f"{user_input} is even")
    else:
        print(f"{user_input} is odd")
else:
    print("Invalid input")
