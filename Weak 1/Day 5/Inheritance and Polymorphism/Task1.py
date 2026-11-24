class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} (Age: {self.age}) is studying {self.course}.")

student = Student("Aarav", 21, "Computer Science")
student.study()