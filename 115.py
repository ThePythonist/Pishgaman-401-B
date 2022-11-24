import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

# age = int(input("Enter an age : "))
# name = input("Enter a name : ")
# phone = input("Enter a phone number : ")

cur.execute("INSERT INTO customers VALUES (20,'Maryam','09336334785');")

# cur.execute("DELETE FROM customers;")
cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
print(records)
# for i in records :
#     print(i[-1])


con.commit()
con.close()
print('Done')
