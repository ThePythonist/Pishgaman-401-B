from Mod import Shape
from math import pi


class Circle(Shape):
    def __init__(self, r):
        super().__init__(r)
        self.radius = r

    def area(self):
        print(self.radius * self.radius * pi)

    def perimeter(self):
        print(self.radius * 2 * pi)


circle = Circle(int(input("Enter radius : ")))
circle.area()
circle.perimeter()
