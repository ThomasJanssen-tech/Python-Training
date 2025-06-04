import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()
cursor.execute("INSERT INTO customers (name,city) VALUES ('Jan', 'Amsterdam')")
cursor.execute("INSERT INTO customers (name,city) VALUES ('Henk', 'Rotterdam')")
cursor.execute("INSERT INTO customers (name,city) VALUES ('Peter', 'Utrecht')")

connection.commit()