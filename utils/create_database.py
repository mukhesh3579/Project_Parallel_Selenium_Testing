import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="Mukesh@3579"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE saucedemo")
print("Database 'saucedemo' created successfully!")
conn.close()