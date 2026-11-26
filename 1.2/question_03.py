# Q9 (Logical Error): Used += instead of = to sum all marks, and used len(marks) * 100 instead of hardcoded 500.
marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / (len(marks) * 100) * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)


# Q10 (Logical Error): Changed = to += so all item prices get added together instead of overwriting total.
cart = [
    ["Keyboard", 800],
    ["Mouse", 400],
    ["USB Cable", 200]
]

total = 0

for item in cart:
    total += item[1]

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
