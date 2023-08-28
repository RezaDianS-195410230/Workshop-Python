Membuat aplikasi web menggunakan python + flask menampilkan table berisi daftar merek motor, harga


1.Instal Flask:
Pastikan  Python dan pip terinstal,Kemudian, instal Flask dengan menjalankan perintah berikut di terminal

pip install Flask

2. Membuat Database
SQLite sebagai database. Buat file bernama motor.db

3. Mendefinisikan Struktur Tabel
membuat tabel dengan kolom 'id', 'merek', 'harga', dan 'fitur' dalam file create_db.py


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

File motor.db yang merupakan database SQLite berisi tabel yang menyimpan informasi tentang merek motor, harga, dan fiturnya. Tabel struktur seperti berikut:

Tabel: motor

id	merek	harga		fitur
1	Honda	15000000	Mesin 150cc
2	Yamaha	14000000	Hemat BBM
3	Suzuki	16000000	Tampilan Sporty

4. Mengisi Data
Buatlah sebuah file insert_data.py untuk memasukkan beberapa data 
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

5. Membuat Aplikasi Flask
Buat file app.py untuk membuat aplikasi Flask

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('motor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT merek, harga, fitur FROM motor')
    motor_data = cursor.fetchall()
    conn.close()
    return render_template('index.html', motor_data=motor_data)

if __name__ == '__main__':
    app.run(debug=True)

6.Membuat Template HTML:
Buat folder templates dalam direktori proyek Anda dan buat file index.html
<!DOCTYPE html>
<html>
<head>
    <title>Daftar Motor</title>
</head>
<body>
    <h1>Daftar Motor</h1>
    <table border="1">
        <tr>
            <th>Merek</th>
            <th>Harga</th>
            <th>Fitur</th>
        </tr>
        {% for motor in motor_data %}
        <tr>
            <td>{{ motor[0] }}</td>
            <td>{{ motor[1] }}</td>
            <td>{{ motor[2] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>

7.Menjalankan Aplikasi
Jalankan aplikasi Flask dengan menjalankan perintah berikut di terminal

python app.py

Buka browser dan akses http://127.0.0.1:5000/ untuk melihat tabel yang menampilkan data motor dari database
