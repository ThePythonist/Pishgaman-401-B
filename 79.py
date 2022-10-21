def tavan(x, y):
    if y == 1:
        return x
    else:
        return x * tavan(x, y - 1)


x, y = int(input("Enter x : ")), int(input("Enter y : "))
print(tavan(x, y))
