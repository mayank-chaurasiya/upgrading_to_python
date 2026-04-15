"""
Problem:
Create a function that returns both the area and
circumference of a circle given its radius.
"""

import math


def circle_stats(radius):
    """Return Area and Circumference of a circle"""
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


RADIUS = int(input("Radius of circle: "))

AREA, CIRCUMFERENCE = circle_stats(RADIUS)

print(
    f"Area is {round(AREA, 2)} and "
    f"Circumference is {round(CIRCUMFERENCE, 2)} "
    f"of circle with radius {RADIUS}"
)
