class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors)
        self.top_speed = top_speed

    def display_details(self):
        print(f"Brand: {self.brand}, Doors: {self.doors}, Top Speed: {self.top_speed} km/h")

ferrari = SportsCar("Ferrari", 2, 340)
ferrari.display_details()