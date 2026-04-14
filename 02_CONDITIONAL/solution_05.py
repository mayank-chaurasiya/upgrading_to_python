"""Weather Activity Suggestion
Problem: Suggest an activity based on the weather
(e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
"""

print("Sunny, Rainy, Snowy")

WEATHER = input("Pick your weather: ")

if WEATHER == "Sunny":
    ACTIVITY = "Go for a walk"
elif WEATHER == "Rainy":
    ACTIVITY = "Read a book"
elif WEATHER == "Snowy":
    ACTIVITY = "Build a snowman"
else:
    ACTIVITY = "none"

print(ACTIVITY)
