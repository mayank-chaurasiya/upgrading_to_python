"""1. Age Group Categorization"""

USER_AGE = int(input("Enter your age: "))

if 0 <= USER_AGE <= 150:
    if USER_AGE < 13:
        print("Child")
    elif USER_AGE < 20:
        print("Teenager")
    elif USER_AGE < 60:
        print("Adult")
    else:
        print("Senior")
else:
    print("Invalid Age")
