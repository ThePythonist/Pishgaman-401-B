items = ["python",12,True]
lst1 = ["sony","samsung","apple"]
lst2 = ["japan","korea","usa"]

# Ex1)
# d = { x:x**2 for x in range(10) }

# Ex2)
# d = { x:type(x) for x in items }

# Ex3)
# dict(lst1,lst2)
d = { k:v for (k,v) in zip(lst1,lst2) }

print(d)
input()
