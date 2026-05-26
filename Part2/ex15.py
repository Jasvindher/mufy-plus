#List of flowers
flowers = ["Rose", "Tulip", "Lily"]
#TODO
# 1. Print a random flower from the list
# 2. Print a random number from 0 to 100
import random
# Print a random flower
random_flower = random.choice(flowers)
print(f"Random flower: {random_flower}")
# Print a random number from 0 to 100
random_number = random.randint(0, 100)
print(f"Random number: {random_number}")