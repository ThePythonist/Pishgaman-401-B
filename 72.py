def func(items):
    numbers = []
    for i in items:
        if type(i) == int or type(i) == float:
            numbers.append(i)

    return numbers


items = [2.3, "toyota", 12, 6.7, "farzad", 5600, ]
print(func(items))
