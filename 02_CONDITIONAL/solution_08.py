"""Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or "Strong".
Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
"""

PASSWORD = input("Your Password: ")
PASSWORD_LENGTH = len(PASSWORD)

if PASSWORD_LENGTH < 6:
    STRENGTH = "Weak"
elif PASSWORD_LENGTH <= 10:
    STRENGTH = "Medium"
else:
    STRENGTH = "Strong"

print(f"Password strength is {STRENGTH}")
