import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()
cursor.execute("SELECT * from customers")

result = cursor.fetchall()

for row in result:
    print(f"ID: {row[0]}, Naam: {row[1]}, Stad: {row[2]}")