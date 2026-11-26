# Q6 (Logical Error): Forgot to return the result from the function, so it printed None.
def square(number):
    result = number * number
    return result

print(square(6))


# Q7 (Logical Error): Changed % 2 == 1 to % 2 == 0 so it adds even numbers instead of odd ones.
numbers = [10, 15, 20, 25, 30, 35]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Even Sum:", total)


# Q8 (Runtime Error): Added ZeroDivisionError handling and moved print inside else so it only runs when there is no error.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
