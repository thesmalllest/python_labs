from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Функция для получения данных из базы данных
def get_db_data(query, params=()):
    conn = sqlite3.connect('excursion_bureau.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    # Получаем все туры
    tours = get_db_data("SELECT * FROM tours")
    return render_template('index.html', tours=tours)

@app.route('/book', methods=['POST'])
def book():
    tourist_name = request.form['name']
    tourist_email = request.form['email']
    tourist_phone = request.form['phone']
    tour_id = request.form['tour_id']
    
    # Вставка нового туриста и бронирования
    conn = sqlite3.connect('excursion_bureau.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tourists (name, email, phone) VALUES (?, ?, ?)", 
                   (tourist_name, tourist_email, tourist_phone))
    conn.commit()
    tourist_id = cursor.lastrowid
    cursor.execute("INSERT INTO bookings (tourist_id, tour_id, booking_date) VALUES (?, ?, CURRENT_DATE)", 
                   (tourist_id, tour_id))
    conn.commit()
    conn.close()
    
    return f"Booking confirmed for {tourist_name}"

# Страница с информацией о туристах
@app.route('/tourists')
def tourists():
    tourists_data = get_db_data("SELECT * FROM tourists")
    return render_template('tourists.html', tourists=tourists_data)

# Страница с информацией о бронированиях
@app.route('/bookings')
def bookings():
    bookings_data = get_db_data('''SELECT tourists.name, tours.title, bookings.booking_date
                                   FROM bookings
                                   JOIN tourists ON bookings.tourist_id = tourists.id
                                   JOIN tours ON bookings.tour_id = tours.id''')
    return render_template('bookings.html', bookings=bookings_data)

# Страница с информацией о турах
@app.route('/all_tours')
def all_tours():
    tours_data = get_db_data("SELECT * FROM tours")
    return render_template('all_tours.html', tours=tours_data)

if __name__ == '__main__':
    app.run(debug=True)
