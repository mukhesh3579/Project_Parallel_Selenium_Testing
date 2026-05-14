import mysql.connector
conn = mysql.connector.connect(
    host=" localhost",
    user="root",
    password="Mukesh@3579",
    database="saucedemo"
)

cursor = conn.cursor()
query = """
CREATE TABLE EMPLOYEE (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    SALARY FLOAT
)
"""

cursor.execute(query)
print("Table 'EMPLOYEE' created successfully!")
conn.close()