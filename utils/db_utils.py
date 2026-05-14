import mysql.connector

def get_login_data():
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mukesh@3579',
        database='saucedemo'
    )

    cursor = conn.cursor()

    query = "SELECT username, password FROM login_users WHERE username like 'standard_user'"

    cursor.execute(query)

    data = cursor.fetchone()
    conn.close()
    return data
 