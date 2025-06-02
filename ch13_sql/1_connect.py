import psycopg2

conn = psycopg2.connect(database="python_training",
                        host="localhost",
                        user="python_training_user",
                        password="python123",
                        port="5432")