import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()
cursor.execute("DELETE FROM customers where name = 'Jan'")

connection.commit()