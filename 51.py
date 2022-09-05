numbers = []
for i in range(3):
    entry = input("Enter any number : ")
    try :
        entry = float(entry)
        numbers.append(entry)
    except ValueError :
        print("That is not a number")
    finally:
        print("Done")

print(numbers)
