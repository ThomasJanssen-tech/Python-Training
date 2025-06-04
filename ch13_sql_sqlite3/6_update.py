import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()
cursor.execute("UPDATE customers SET city = 'Den Haag' WHERE name = 'Jan'")

connection.commit()