a,b = 0,1

for i in range(10000):
    print(a)
    # c = a
    # a = b
    # b = c+b

    a,b = b,a+b


