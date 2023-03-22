class User:
    def __init__(self,id, username, name, surname, email, pass_hash, role_id):
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.pass_hash = pass_hash
        self.role_id = role_id

    def __str__(self):
        return f'id: {self.id}, Username: {self.username}, Name: {self.name}, Surname: {self.surname}, Email: {self.email},Pass: {self.pass_hash} Role: {self.role_id}'

    def to_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.pass_hash,
            'role': self.role_id
        }
