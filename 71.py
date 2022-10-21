def pangram(word):
    if len(word) == len(set(word)):
        return True
    else:
        return False


name = input("Enter your name : ")
print(pangram(name))

if pangram(name) == True:
    print("Victory")
else:
    print("Failed")
