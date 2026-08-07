import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="252800",
    database="studentdb"
)
cursor=connection.cursor()
print("Database connected successfully")