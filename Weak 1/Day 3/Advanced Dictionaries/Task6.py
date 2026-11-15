employee_salaries = {"Alice": 70000, "Bob": 50000, "Charlie": 90000, "Dave": 60000, "Eve": 85000}

sorted_employees = sorted(employee_salaries.items(), key=lambda item: item[1], reverse=True)
print("Top 3 Highest Paid:", sorted_employees[:3])