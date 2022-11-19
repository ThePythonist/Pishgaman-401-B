import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute("CREATE TABLE customers (age INT, name VARCHAR(50), phone VARCHAR(50));")
cur.execute("INSERT INTO customers VALUES (16,'Arian','09353334325');")

# cur.execute("DELETE FROM customers;")
cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
# print(records)
for i in records :
    print(i[-1])


con.commit()
con.close()
print('Done')
