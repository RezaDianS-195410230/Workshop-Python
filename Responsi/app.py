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
