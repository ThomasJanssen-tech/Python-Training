import psycopg2

conn = psycopg2.connect(database="python_training",
                        host="localhost",
                        user="python_training_user",
                        password="python123",
                        port="5432")


#conn.autocommit = True

user_id = 2

cursor = conn.cursor()
cursor.execute("SELECT * from klanten WHERE id = %s", (user_id,))

result = cursor.fetchall()

for row in result:
    print(f"ID: {row[0]}, Naam: {row[1]}, Stad: {row[2]}")