import psycopg2

conn = psycopg2.connect(database="python_training",
                        host="localhost",
                        user="python_training_user",
                        password="python123",
                        port="5432")


#conn.autocommit = True

cursor = conn.cursor()
cursor.execute("DELETE FROM klanten WHERE naam = 'Jan'")

conn.commit()