"""Generator Function with yield
Problem: Write a generator function that yields
even numbers up to a specified limit.
"""


def even_generator(limit):
    """Generate even numbers upto a specified limits"""
    yield from range(2, limit + 1, 2)


for num in even_generator(10):
    print(num, end=" ")
