def power(a, b):
    print(a ** b)


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
