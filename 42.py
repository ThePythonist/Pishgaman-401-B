n = int(input("How many numbers do you want to enter : "))
numbers = []

for i in range(n):
    number = int(input("Enter any number : "))
    numbers.append(number)

print(max(numbers))
