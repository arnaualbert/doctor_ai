# from flask_login import UserMixin
# UserMixin    

class User:
    def __init__(self, username, name, surname, email, password, role):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return f'Username: {self.username}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Role: {self.role}'

    def to_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
