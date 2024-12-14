import sqlite3

# Подключение к базе данных (если базы нет, она будет создана)
conn = sqlite3.connect('excursion_bureau.db')
cursor = conn.cursor()

# Создание таблицы туристов
cursor.execute('''CREATE TABLE IF NOT EXISTS tourists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT
                )''')

# Создание таблицы туров
cursor.execute('''CREATE TABLE IF NOT EXISTS tours (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL
                )''')

# Создание таблицы бронирований
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tourist_id INTEGER,
                    tour_id INTEGER,
                    booking_date TEXT,
                    FOREIGN KEY (tourist_id) REFERENCES tourists (id),
                    FOREIGN KEY (tour_id) REFERENCES tours (id)
                )''')

# Подтверждение изменений и закрытие соединения
conn.commit()
conn.close()

print("Database and tables created successfully!")
