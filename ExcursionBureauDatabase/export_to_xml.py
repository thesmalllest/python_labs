import sqlite3
from xml.dom.minidom import Document

# Подключение к базе данных
conn = sqlite3.connect('excursion_bureau.db')
cursor = conn.cursor()

# Запрос всех туров
cursor.execute("SELECT * FROM tours")
tours = cursor.fetchall()

# Создание XML документа
doc = Document()
root = doc.createElement("tours")
doc.appendChild(root)

# Добавление данных о турах в XML
for tour in tours:
    tour_element = doc.createElement("tour")
    root.appendChild(tour_element)
    
    id_element = doc.createElement("id")
    id_element.appendChild(doc.createTextNode(str(tour[0])))
    tour_element.appendChild(id_element)

    title_element = doc.createElement("title")
    title_element.appendChild(doc.createTextNode(tour[1]))
    tour_element.appendChild(title_element)

    description_element = doc.createElement("description")
    description_element.appendChild(doc.createTextNode(tour[2]))
    tour_element.appendChild(description_element)

    price_element = doc.createElement("price")
    price_element.appendChild(doc.createTextNode(str(tour[3])))
    tour_element.appendChild(price_element)

# Сохранение XML в файл
with open("tours.xml", "w") as f:
    f.write(doc.toprettyxml())

# Закрытие соединения
conn.close()

print("Data exported to XML successfully!")
