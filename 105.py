from random import choice


def generate1():
    password = []

    for i in range(6):
        x = str(choice(range(10)))
        password.append(x)

    password = "".join(password)
    print(password)


generate1()


#----------------------------------------

def generate2():
    password = ""

    for i in range(6):
        x = str(choice(range(10)))
        password += x

    print(password)


generate2()
