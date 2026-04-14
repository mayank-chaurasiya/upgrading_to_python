"""Leap Year Checker
Problem: Determine if a year is a leap year.
(Leap years are divisible by 4, but not by 100 unless also divisible by 400).
"""

YEAR = int(input("Your Year : "))

if ((YEAR % 4 == 0) and (YEAR % 100 != 0)) or (YEAR % 400 == 0):
    print(f"{YEAR} is Leap Year")
else:
    print(f"{YEAR} is not Leap Year")
