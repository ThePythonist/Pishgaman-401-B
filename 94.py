lines = open('words.txt').readlines()
rev = [ line[::-1] for line in lines]
print(rev[:100])
