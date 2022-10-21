def func(a, b):
    # a = str(a)
    # b = str(b)
    # print(a+"."+b)

    # output = float("{}.{}".format(a, b))
    output = float(f"{a}.{b}")
    print(type(output))
    print(output)


a = int(input("Enter Integer : "))
b = int(input("Enter Decimal : "))
func(a, b)
