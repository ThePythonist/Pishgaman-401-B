# def is_even(number):
#     divs = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divs.append(i)
#
#     if len(divs) == 2:
#         return True
#     else:
#         return False

def is_prime(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    # return True if len(divs) == 2 else False
    print(True) if len(divs) == 2 else print(False)


n = int(input("Enter any number : "))
# print(is_prime(n))
is_prime(n)
