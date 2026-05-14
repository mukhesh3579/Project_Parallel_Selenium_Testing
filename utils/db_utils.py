from pymongo import MongoClient

def get_login_data():
    # 
    client = MongoClient('mongodb://localhost:27017/')

    db = client['saucedemo']
    collection = db['login_users']

    user = collection.find_one()
    client.close()
    return user['username'], user['password']

    









































#import mysql.connector

#def get_login_data():
    # Establish a connection to the MySQL database
    #conn = mysql.connector.connect(
        #host='localhost',
        #user='root',
        #password='Mukesh@3579',
        #database='saucedemo'
    #)

    #cursor = conn.cursor()

    #query = "SELECT username, password FROM login_users WHERE username like 'standard_user'"

    #cursor.execute(query)

    #data = cursor.fetchone()
    #conn.close()
    #return data
 