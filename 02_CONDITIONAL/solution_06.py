"""Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance
(e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
"""

DISTANCE = int(input("Enter your distance: "))

if DISTANCE < 3:
    TRANSPORT_MODE = "Walk"
elif DISTANCE < 15:
    TRANSPORT_MODE = "Bike"
elif DISTANCE >= 15:
    TRANSPORT_MODE = "Car"
else:
    TRANSPORT_MODE = "None"

print(TRANSPORT_MODE)
