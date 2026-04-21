"""Write a program to check if a given year is a leap year"""

YEAR = int(input("Your Year : "))

if ((YEAR % 4 == 0) and (YEAR % 100 != 0)) or (YEAR % 400 == 0):
    print(f"{YEAR} is Leap Year")
else:
    print(f"{YEAR} is not Leap Year")
