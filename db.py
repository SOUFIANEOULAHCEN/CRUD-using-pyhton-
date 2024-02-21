import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute("CREATE TABLE users (ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,EMAIL TEXT NOT NULL)")
con.commit()
con.close()