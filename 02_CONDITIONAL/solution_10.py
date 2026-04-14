"""Pet Food Recommendation
Problem: Recommend a type of pet food based on the pet's species and age.
(e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
"""

PET_SPECIES = input("your pet species: ")

if PET_SPECIES in {"Dog", "Cat"}:
    PET_AGE = int(input("Pet's age: "))
    if PET_SPECIES == "Dog":
        if PET_AGE < 2:
            print("puppy food")
        else:
            print("Food not found")
    else:
        if PET_AGE > 5:
            print("Senior cat food")
        else:
            print("Food not found")

else:
    print("No data for this species")
