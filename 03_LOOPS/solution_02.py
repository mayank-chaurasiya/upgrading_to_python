"""Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.
"""

n = int(input("Enter your number: "))
sum_even = 0

for num in range(n):
    if num % 2 == 0:
        sum_even += num

print(f"sum of even numbers up to {n} is {sum_even}")
