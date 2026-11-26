# Q1 (Syntax Error): Missed a closing bracket ")" at the end of the second input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum:", sum)


# Q2 (Logical Error): Used + instead of * to calculate the area.
length = 10
width = 5

area = length * width

print("Area:", area)


# Q3 (Logical Error): range(1, 10) stops at 9, so changed it to 11 to include 10.
for i in range(1, 11):
    print(i)


# Q4 (Logical Error): Swapped "Odd" and "Even" since remainder 0 means the number is even.
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q5 (Runtime Error): Index 4 is out of range for a 4-item list, so used -1 to get the last item.
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])
