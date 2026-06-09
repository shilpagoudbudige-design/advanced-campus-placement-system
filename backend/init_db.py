import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
conn.execute(
    "INSERT INTO users (email, password) VALUES (?, ?)",
    ("shilpa@gmail.com", "123456")
)

conn.commit()
print("User Added Successfully!")

conn.close()