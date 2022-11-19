# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
# b = B()
# b.say_hello()
# b.say_goodbye()


# Super()

class Pedar:
    def __init__(self, fname, address, eyecolor):
        self.familyname = fname
        self.address = address
        self.eyecolor = eyecolor

    def say_hello(self):
        print("Hello")


class Farzand(Pedar):
    def __init__(self, fname, address, eyecolor, height, weight):
        super().__init__(fname, address, eyecolor)
        self.height = height
        self.weight = weight

    def say_goodbye(self):
        print("Goodbye")


height = int(input("Enter a height : "))
weight = int(input("Enter a weight : "))

pesar = Farzand("Ahmadi", "Ekbatan, Faz1", "Black", height, weight)
# pesar.say_goodbye()
# pesar.say_hello()
print(pesar.familyname)
print(pesar.address)
print(pesar.eyecolor)
print(pesar.height)
print(pesar.weight)
