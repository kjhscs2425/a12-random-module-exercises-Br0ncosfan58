import random

# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["dog", "cat", "hamster"])
# Age (integer)
age = random.randint(1, 15)
# Color (at least 3 choices, string)
color = random.choice(["brown", "black", "white"])
# Weight (float)
weight = random.uniform(1, 100)

# Print a summary of your pet using an f-string
print(f"Your pet is a {color} {animal} that is {age} years old and weighs {weight} pounds.")