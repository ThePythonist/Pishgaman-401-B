from math import pi


class Shape:
    def __init__(self, l=0, w=0, r=0):
        self.length = l
        self.width = w
        self.radius = r

    def rec_area(self):
        print(self.length * self.width)

    def rec_perimeter(self):
        print((self.length + self.width) * 2)

    def circle_area(self):
        print(self.radius * self.radius * pi)

    def circle_perimeter(self):
        print(self.radius * 2 * pi)


# l = int(input("Enter length : "))
# w = int(input("Enter width : "))
# rectangle = Shape(l, w)
# rectangle.rec_area()
# rectangle.rec_perimeter()

r = int(input("Enter radius : "))
circle = Shape(r=r)
circle.circle_perimeter()
circle.circle_area()
