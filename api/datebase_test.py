import sqlite3

conn=sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER
                )''')

conn.commit()
conn.close

conn=sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?,?)', ("Jacob",18))

conn.commit()
conn.close
