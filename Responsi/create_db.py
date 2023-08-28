import sqlite3

conn = sqlite3.connect('motor.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE motor (
        id INTEGER PRIMARY KEY,
        merek TEXT,
        harga INTEGER,
        fitur TEXT
    )
''')

conn.commit()
conn.close()
