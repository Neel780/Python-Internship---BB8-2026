import random

random_integers = [random.randint(1, 100) for _ in range(15)]
unique_integers = []

for num in random_integers:
    if num not in unique_integers:
        unique_integers.append(num)

print("Original:", random_integers)
print("Unique (ordered):", unique_integers)