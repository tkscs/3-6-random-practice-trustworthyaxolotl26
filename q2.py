import random

# Make a random pet.

# Choose:
# Type of animal (at least 3 choices, string)
animal = ["fox", "cat", "otter"]
# Age (integer)
age = [random.randint(2, 12)]
# Color (at least 3 choices, string)
eye_color = ["blue", "green", "browwn", "yellow" ]
# Weight (float)
weight = [random.uniform(1, 5)]

# Print a summary of your pet using an f-string
print(f"Your pet is a baby {random.choice(animal)}, who is {random.choice(age)} months old, weighs {random.choice(weight)} pounds, and has {random.choice(eye_color)} eyes")
