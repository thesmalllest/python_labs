import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('excursion_bureau.db')
cursor = conn.cursor()

# Статистический запрос 1: Получение всех туристов
cursor.execute("SELECT * FROM tourists")
tourists = cursor.fetchall()
print("All Tourists:")
for tourist in tourists:
    print(tourist)

# Статистический запрос 2: Получение всех туров с их ценами
cursor.execute("SELECT title, price FROM tours")
tours = cursor.fetchall()
print("\nAll Tours:")
for tour in tours:
    print(f"{tour[0]} - ${tour[1]}")

# Статистический запрос 3: Получение информации о бронированиях
cursor.execute('''SELECT tourists.name, tours.title, bookings.booking_date
                  FROM bookings
                  JOIN tourists ON bookings.tourist_id = tourists.id
                  JOIN tours ON bookings.tour_id = tours.id''')
bookings = cursor.fetchall()
print("\nAll Bookings:")
for booking in bookings:
    print(f"{booking[0]} booked {booking[1]} on {booking[2]}")

# Закрытие соединения
conn.close()
