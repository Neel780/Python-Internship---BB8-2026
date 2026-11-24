class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False

rect1 = Rectangle(4, 6)
rect2 = Rectangle(3, 8)
print("Are rectangles equal?", rect1 == rect2)