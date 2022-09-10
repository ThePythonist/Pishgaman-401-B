# n = int(input("How many numbers do you want to enter : "))
# numbers = []
#
# for i in range(n):
#     number = int(input("Enter any number : "))
#     numbers.append(number)
#
# print(max(numbers))

end = False
numbers = []

# while end == False:
while not end:
    number = input("Enter any number : ")
    if number == "stop":
        end = True
    else:
        try :
            number = int(number)
            numbers.append(number)
        except ValueError :
            print("Invalid Input")

try :
    print("Maximum :",max(numbers))
except ValueError:
    print("The list was empty")
