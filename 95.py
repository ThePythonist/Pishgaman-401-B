def signup(user, pw):
    open("DB-USERS.txt", "a+").write(user + "\n")
    open("DB-PASSWORDS.txt", "a+").write(pw + "\n")
    print("Account Created")


def login(user, pw):
    db_usernames = open("DB-USERS.txt", "r").readlines()
    db_passwords = open("DB-PASSWORDS.txt", "r").readlines()
    usernames = [user[:-1] for user in db_usernames]
    passwords = [password[:-1] for password in db_passwords]
    accounts = dict(zip(usernames, passwords))

    if user in accounts:
        if pw == accounts[user]:
            print("Login completed")
        else:
            print("Password was incorrect try again")
    else:
        print("Account not found")


operation = input("Choose your action \n"
                  "1 : Signup , 2 : Login : ")
if operation == "1":
    user = input("Enter username : ").casefold()
    pw = input("Enter password : ")
    signup(user,pw)
elif operation == "2":
    user = input("Enter username : ").casefold()
    pw = input("Enter password : ")
    login(user,pw)
else :
    print("Invalid Input")
