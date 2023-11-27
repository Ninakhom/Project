import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="res"
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as e:
        print(e)
        return None

def close_connection(connection):

    if connection:
        connection.close()
        print("Connection closed")

def get_cursor(connection):

    if connection:
        return connection.cursor()
    else:
        return None
