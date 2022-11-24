import sqlite3

con = sqlite3.connect('test2.db')
cur = con.cursor()

# cur.execute("""
# CREATE TABLE employees (
# id INT,
# fname VARCHAR(50),
# lname VARCHAR(50),
# age INT,
# job VARCHAR(50)
# );
# """)

# people = [
#     {"Fname": "Yasamin", "Lname": "Aghasaleh", "Age": 15, "Job": "Front-End Dev"},
#     {"Fname": "Shayan", "Lname": "Ghari", "Age": 15, "Job": "Front-End Dev"},
#     {"Fname": "Ilia", "Lname": "Seyfollahi", "Age": 15, "Job": "Back-End Dev"},
#     {"Fname": "Sajad", "Lname": "Mohammadi", "Age": 18, "Job": "DB Man"},
#     {"Fname": "Benyamin", "Lname": "Medghalchi", "Age": 15, "Job": "Security Engineer"},
#     {"Fname": "Arash", "Lname": "Sadeghi", "Age": 21, "Job": "Back-End Dev", },
#     {"Fname": "Laleh", "Lname": "Saboktakin", "Age": 0, "Job": "Back-End Dev", }
# ]
#
# id = 1100
#
# for person in people:
#     cur.execute(f"INSERT INTO employees VALUES (?,?,?,?,?)",
#                 (id, person["Fname"], person["Lname"], person["Age"], person["Job"]))
#     id += 1
#     con.commit()

# cur.execute("DELETE FROM employees;")
cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
# print(len(records))
# print(records)
for record in records :
    print(record)

con.commit()
con.close()
print('Done')