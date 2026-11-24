class Employee:
    def calculate_salary(self):
        return 50000

class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 15000

class Designer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 10000

dev = Developer()
des = Designer()

print("Developer Salary:", dev.calculate_salary())
print("Designer Salary:", des.calculate_salary())