# morakab = []
# adad = [ i for i in range(2,100) ]
#
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0 :
#             morakab.append(i)
#             break
#
# print(set(adad).difference(morakab))

#------------------------------------------------

primes = []
a,b = int(input("Start : ")),int(input("End : "))

for i in range(a,b):
    if i > 1 :
        for j in range(2,i):
            if i % j == 0 :
                break
        else :
            primes.append(i)

print(primes)
