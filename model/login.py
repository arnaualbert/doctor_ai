import model.user as user
from typing import Union
import model.database as databases
import mysql.connector
import hashlib

### Connect to the database
conexion = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="1234",
    database="doctor_ai"
)


data = databases.Database("localhost","admin","1234","doctor_ai")

def login(username: str, password:str) -> Union[bool, user.User]:
    """
    Log in the user
        Parameters:
            username (str): The username that wants to log in
            password (str): The password of the password that wants to log in
        Returns:
            bool: True if the login was successful, False otherwise
    """
    enc_pass = hashlib.sha256(password.encode()).hexdigest()
    resultado = data.query(f'SELECT * FROM users WHERE username="{username}" AND pass_hash="{enc_pass}"')
    if resultado is None:
        return False
    else:
        return user.User(*resultado)

def register(username: str,name: str,surname: str,email: str,password: str,role_id: int) -> bool:
    """
    Registers a new user with the provided information.

        Parameters:
            username (str):  The username for the new user.
            name (str): The name of the new user.
            surname (str): The surname of the new user.
            email (str): The email address of the new user.
            password (str): The password for the new user.
            role_id (int): The role ID for the new user.
        Returns:
            True if the user was registered successfully, False otherwise.
    """
    resultado = data.query(f"SELECT * FROM users WHERE username = '{username}'")
    if resultado is None:
        data.query(f"INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES ('{username}','{name}','{surname}','{email}','{password}',{role_id})")
        data.commit()
        return True
    else:
        return False

