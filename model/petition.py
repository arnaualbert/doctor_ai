class Petition:
    '''Petition class'''
    def __init__(self, admin_petition, username, name, surname, email, role):
        self.admin_petition = admin_petition
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.role = role
        
    def __str__(self):
        return f'id: {self.admin_petition}, Username: {self.username}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Role: {self.role}'

    def to_dict(self):
        return {
            'admin_petition': self.admin_petition,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'role': self.role
        }