import model.user as user
from typing import Union
from flask  import session
import model.database as databases
import mysql.connector
import hashlib
import model.scripts as tools

### Connect to the database
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="doctor_ai"
)


data = databases.Database("localhost","root","","doctor_ai")

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
    print(
        enc_pass
    )
    resultado = data.query(f'SELECT * FROM users WHERE username="{username}" AND pass_hash="{enc_pass}"')
    if resultado is None:
        return False
    else:
        return tools.tuple_to_object(resultado)

def register(user: user.User) -> bool:
    """
    Registers a new user with the provided information.

        Parameters:
            user (user.User): The user that wants to register
        Returns:
            True if the user was registered successfully, False otherwise.
    """
    resultado = data.query(f"SELECT * FROM users WHERE username = '{user.username}'")
    if resultado is None:
        data.query(f"INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES ('{user.username}','{user.name}','{user.surname}','{user.email}','{user.pass_hash}',{user.role_id})")
        data.commit()
        return True
    else:
        return False

def is_logged():
    if session.get('username') != None:
        return True
    else:
        return False
    
def get_user_data_from_database(username)-> Union[bool, user.User]:

    # ejecutar una consulta para recuperar los datos del usuario
    result = data.query(f"SELECT * FROM users WHERE username = '{username}'")
    if result is None:
        return False
    else:
        return tools.tuple_to_object(result)


def edit(username, name, surname, email) -> bool:

    data.query(f"UPDATE users SET name = '{name}',surname = '{surname}',email = '{email}' WHERE username='{username}'")
    data.commit()
    
    return True
