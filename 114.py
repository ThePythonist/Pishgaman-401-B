import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute("CREATE TABLE customers (age INT, name VARCHAR(50), phone VARCHAR(50));")

con.commit()
con.close()
print('Done')
