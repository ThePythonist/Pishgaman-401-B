lines = open("words.txt").readlines()

for line in lines :
    if len(line) == 6 :
        print(line)

