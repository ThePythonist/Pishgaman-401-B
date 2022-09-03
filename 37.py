numbers = [12,4,3,1,5,14,8]
# evens = []
evens = list()

for number in numbers :
    if number % 2 == 0 :
        # evens.append(number)
        evens += [number]

print(evens)
