class Car:
    def __init__(self, c, m):
        # print("hello from init")
        self.color = c
        self.model = m

    def tormoz(self):
        print("Breaaak!")

    def warn(self):
        print("darb khodro baz ast")

    def tell_info(self):
        print(self.color)
        print(self.model)


samand = Car("white", "soren")
persia = Car("black", "tu5")

samand.warn()
# persia.tormoz()
# print(samand.color)
# persia.tell_info()
