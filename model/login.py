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
    if resultado is None:
        return False
    else:
        return user.User(*resultado)

def register(username: str,name: str,surname: str,email: str,password: str,role_id: int) -> bool:
    """Register a new user
    @param username: username
    @param name: name
    @param surname: surname
    @param email: email
    @param password: password
    @param role_id: role id
    @return: True or False
    """
    resultado = data.query(f"SELECT * FROM users WHERE username = '{username}'")
    if resultado is None:
        data.query(f"INSERT INTO users (username,name,surname,email,pass_hash,role_id) VALUES ('{username}','{name}','{surname}','{email}','{password}',{role_id})")
        return True
    else:
        return False
