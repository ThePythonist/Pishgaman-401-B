def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


entry = int(input("Enter any number : "))
if entry > 0:
    print(factorial(entry))
elif entry == 0:
    print("Factorial of zero is 1")
elif entry < 0:
    print("Factorial does not exist")
