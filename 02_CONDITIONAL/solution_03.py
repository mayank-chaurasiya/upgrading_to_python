"""Grade Calculator
Problem: Assign a letter grade based on a student's score:
A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
"""

STUDENT_SCORE = int(input("Enter score: "))

if 0 <= STUDENT_SCORE <= 100:
    if 90 <= STUDENT_SCORE <= 100:
        print("Your Grade is A")
    elif 80 <= STUDENT_SCORE <= 89:
        print("Your Grade is B")
    elif 70 <= STUDENT_SCORE <= 79:
        print("Your Grade is C")
    elif 60 <= STUDENT_SCORE <= 69:
        print("Your Grade is D")
    else:
        print("Your Grade is F")
else:
    print("Invalid Score")
