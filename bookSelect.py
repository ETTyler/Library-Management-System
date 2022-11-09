import sqlite3

db = sqlite3.connect('Library.db')
cursor = db.cursor()

res = cursor.execute("SELECT * FROM Books")
for row in res:
    print(row)
