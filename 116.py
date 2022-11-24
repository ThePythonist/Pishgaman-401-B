import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

# cur.execute("DELETE FROM customers;")
cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
# print(records)
for i in records:
    print(i[-1])

con.commit()
con.close()
print('Done')
