import mysql.connector
conn = None
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mukesh@3579",
        database="saucedemo"
    )
    cursor = conn.cursor()

    cursor.execute("UPDATE EMPLOYEE SET SALARY = 60000 WHERE NAME = 'Mukesh'")
    conn.commit()

except:
    print("database connection failed")
finally:
    if conn and conn.is_connected():
        conn.close()
        print("database connection closed")