import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mukesh@3579",
    database="saucedemo"
)

values = ["Mukesh", 50000]
print("connected with db")
cursor = conn.cursor()
sql = """INSERT INTO EMPLOYEE (NAME, SALARY) VALUES (%s, %s)"""
cursor.execute(sql, values)
conn.commit()
print("Data inserted successfully!")
conn.close()