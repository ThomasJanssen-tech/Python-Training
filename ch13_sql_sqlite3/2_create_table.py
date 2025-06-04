import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE "customers" (
	"id"	INTEGER UNIQUE,
	"name"	TEXT,
	"city"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""")

connection.commit()