items = ["italy", "spain", 200, 12.5, "england", 8]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float :
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
