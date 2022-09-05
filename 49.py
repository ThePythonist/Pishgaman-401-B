number = int(input("Enter any number : "))
# divisors = []
#
# for n in range(1,number+1):
#     if number % n == 0 :
#         divisors.append(n)
#
# print(divisors)

divisors = [i for i in range(1,number+1) if number % i == 0]

if divisors == [1,number]:
    print("Prime")
else :
    print("Not Prime")
