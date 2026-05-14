import mysql.connector
import mysql 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukesh@3579",
    database="ecommerce"
)

print("Database connection successful!")
conn.close()