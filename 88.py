lines = open("words.txt", "r").readlines()
# lines.sort(key=len)
# print(lines[-1])
# print(len(lines[-1]))

maximum = max(lines, key=len)
minimum = min(lines, key=len)
print("Longest :",maximum)
print("Shortest :",minimum)

print('------------------------')

for line in lines :
    if len(line) == len(maximum):
        print(line)
