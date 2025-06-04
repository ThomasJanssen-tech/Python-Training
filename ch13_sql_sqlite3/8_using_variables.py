import sqlite3

connection = sqlite3.connect('example.db')

user_id = 2

cursor = connection.cursor()

data = [user_id]

cursor.execute("SELECT * from customers WHERE id = ?", data)

result = cursor.fetchall()

for row in result:
    print(f"ID: {row[0]}, Naam: {row[1]}, Stad: {row[2]}")