import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('excursion_bureau.db')
cursor = conn.cursor()

# Вставка данных о туристах
cursor.execute("INSERT INTO tourists (name, email, phone) VALUES ('Alice Smith', 'alice@example.com', '1234567890')")
cursor.execute("INSERT INTO tourists (name, email, phone) VALUES ('Bob Johnson', 'bob@example.com', '0987654321')")

# Вставка данных о турах
cursor.execute("INSERT INTO tours (title, description, price) VALUES ('Mountain Hiking', 'Hiking in the beautiful mountain range.', 200.0)")
cursor.execute("INSERT INTO tours (title, description, price) VALUES ('City Tour', 'Guided tour of the historic city center.', 50.0)")

# Вставка данных о бронированиях
cursor.execute("INSERT INTO bookings (tourist_id, tour_id, booking_date) VALUES (1, 1, '2024-12-14')")
cursor.execute("INSERT INTO bookings (tourist_id, tour_id, booking_date) VALUES (2, 2, '2024-12-15')")

# Подтверждение изменений и закрытие соединения
conn.commit()
conn.close()

print("Data inserted successfully!")
