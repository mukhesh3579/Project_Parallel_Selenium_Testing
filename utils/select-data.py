
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukesh@3579",
    database="saucedemo"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM EMPLOYEE")
results = cursor.fetchall()
for row in results:
    print(row)