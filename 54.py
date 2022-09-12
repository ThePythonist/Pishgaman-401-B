info = {
	"fname":"taha",
	"lname":"hosseini",
	"city":"shiraz",
	"age":27,
	"blood":"o+"
}

key = input("Enter any key to search in dictionary : ")

try :
	print(key,":",info[key])

except KeyError :
	print("Key not found")
