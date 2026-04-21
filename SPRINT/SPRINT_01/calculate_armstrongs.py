"""Write a program to check if a number is an Armstrong number."""

user_input = int(input("Your Number: "))

if 0 <= user_input <= 9:
    print(f"{user_input} is Armstrong Number")
elif user_input < 0:
    print("Invalid Number")
else:
    temp = user_input
    order = 0
    while temp != 0:
        order += 1
        temp = temp // 10

    temp = user_input
    armstrong_sum = 0
    while temp != 0:
        last_digit = temp % 10
        armstrong_sum = armstrong_sum + (last_digit**order)
        temp = temp // 10

    if armstrong_sum == user_input:
        print(f"{user_input} is Armstrong number")
    else:
        print(f"{user_input} is not Armstrong number")
