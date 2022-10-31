# lines = open('words.txt').readlines()
# items = []
#
# for line in lines :
#     items.append(line[0:-1])
#
# print(items[:1000])

lines = open('words.txt').readlines()
items = []
for line in lines :
    items.append(line.replace("\n",""))

print(items)
