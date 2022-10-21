def f(x, y):
    if y == 1:
        return 1 + x
    else:
        return 1 + f(x, y - 1)


print(f(2, 4))
