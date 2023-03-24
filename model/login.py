import model.user as user
from typing import Union
import model.database as databases

data = databases.Database("localhost","root","","doctor_ai")

def login(username: str, password:str) -> Union[bool, user.User]:
    """Log in the user
    @param username: username
    @param password: password
    @return: user or False
    """
    resultado = data.query(f'SELECT * FROM users WHERE username="{username}" AND pass_hash="{password}"')
    print(resultado)
    if resultado is None:
        return False
    else:
        return user.User(*resultado)

def register(username: str,name: str,surname: str,email: str,password: str,role_id: int) -> bool:
    """Register a new user"""
    # cursor = conexion.cursor()
    # cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    # resultado = cursor.fetchone()
    resultado = data.query(f"SELECT * FROM users WHERE username = '{username}'")
    if resultado is None:
        data.query(f"INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES ('{username}','{name}','{surname}','{email}','{password}',{role_id})")
        # cursor.execute("INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES (%s,%s,%s,%s,%s,%s)",(username,name,surname,email,password,role_id))
        # conexion.commit()
        return True
    else:
        return False
