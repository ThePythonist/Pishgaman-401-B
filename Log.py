x = input("Enter a number : ")

try:

    x = int(x)
    try:
        print(x[0])
    except Exception as error:
        print("Nemitavan index gereft")
        open("Log.txt", "a+").write(str(error))

except ValueError:
    print("عدد وارد کنید")
