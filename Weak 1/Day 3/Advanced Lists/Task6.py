numbers = [10, 45, 2, 99, 50, 75]
largest = float('-inf')
second_largest = float('-inf')

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("Second largest number:", second_largest)