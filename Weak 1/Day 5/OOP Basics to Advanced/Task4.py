class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Salary updated to {self.__salary}")
        else:
            print("Error: New salary must be greater than the current salary.")

emp = Employee(50000)
print("Current Salary:", emp.get_salary())
emp.set_salary(60000)
emp.set_salary(45000)