def calculator(n1, op, n2):
    def add():
        return n1 + n2

    def subtract():
        return n1 - n2

    def multiply():
        return n1 * n2

    def divide():
        return n1 / n2

    if op == "+":
        print(add())
    elif op == "-":
        print(subtract())
    elif op == "*":
        print(multiply())
    elif op == "/":
        print(divide())
    else:
        print("Invalid Input Try Again")
        # calculator()


n1 = int(input("Enter number 1 : "))
op = input("Enter any operator : ")
n2 = int(input("Enter number 2 : "))

calculator(n1, op, n2)
