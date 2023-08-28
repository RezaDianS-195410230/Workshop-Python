import sqlite3

conn = sqlite3.connect('motor.db')
cursor = conn.cursor()

data = [
    ('Honda', 15000000, 'Mesin 150cc'),
    ('Yamaha', 14000000, 'Hemat BBM'),
    ('Suzuki', 16000000, 'Tampilan Sporty'),
]

cursor.executemany('INSERT INTO motor (merek, harga, fitur) VALUES (?, ?, ?)', data)

conn.commit()
conn.close()
