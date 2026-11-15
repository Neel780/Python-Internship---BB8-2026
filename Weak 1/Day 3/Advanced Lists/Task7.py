employees = ["Alice", "Bob", "Charlie"]
salaries = [50000, 60000, 75000]

for emp, salary in zip(employees, salaries):
    print(f"{emp}: {salary}")