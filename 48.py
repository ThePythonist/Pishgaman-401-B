number = 12
# divisors = []
#
# for n in range(1,number+1):
#     if number % n == 0 :
#         divisors.append(n)

divisors = [i for i in range(1,number+1) if number % i == 0]
print(divisors)
