import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Cambia por tu contraseña
        database="store_db"
    )
    return connection
