import psycopg2

conn = psycopg2.connect(database="python_training",
                        host="localhost",
                        user="python_training_user",
                        password="python123",
                        port="5432")


#conn.autocommit = True

cursor = conn.cursor()
cursor.execute("INSERT INTO klanten (naam,stad) VALUES ('Jan', 'Amsterdam')")
cursor.execute("INSERT INTO klanten (naam,stad) VALUES ('Henk', 'Rotterdam')")
cursor.execute("INSERT INTO klanten (naam,stad) VALUES ('Peter', 'Utrecht')")

conn.commit()