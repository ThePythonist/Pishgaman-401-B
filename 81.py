import math

def greetings(name):
    return "hello" + " " + name


# Aliasing
ahvalporsi = greetings
# print(ahvalporsi("Nima"))
# print(greetings("Sepideh"))
# print(ahvalporsi)
# print(greetings)

jazr = math.sqrt
# print(jazr(100))

chap = print
chap(jazr(100))
