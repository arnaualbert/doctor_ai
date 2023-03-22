import mysql.connector
import model.user as user
from typing import Union

### Connect to the database
conexion = mysql.connector.connect(
    host="localhost",
    user="vic",
    password="123qwe",
    database="doctor_ai"
)


def login(username, password) -> Union[bool, user.User]:
    """Log in the user
    @param username: username
    @param password: password
    """
    #create a cursor
    cursor = conexion.cursor()
    # Verify if the user is correct
    cursor.execute("SELECT * FROM users WHERE username=%s AND pass_hash=%s", (username, password))
    resultado = cursor.fetchone()
    if resultado is None:
        return False
    else:
        return user.User(*resultado)

def register(username,name,surname,email,password,role_id):
    """Register a new user"""
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    resultado = cursor.fetchone()
    if resultado is None:
        cursor.execute("INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES (%s,%s,%s,%s,%s,%s)",(username,name,surname,email,password,role_id))
        conexion.commit()
        return True
    else:
        return False