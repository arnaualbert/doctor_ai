class User:
    '''User class'''
    def __init__(self,id, username, name, surname, email, pass_hash, role_id):
        self._id = id
        self._username = username
        self._name = name
        self._surname = surname
        self._email = email
        self._pass_hash = pass_hash
        self._role_id = role_id
        
    def __str__(self):
        return f'id: {self._id}, Username: {self._username}, Name: {self._name}, Surname: {self._surname}, Email: {self._email},Pass: {self._pass_hash} Role: {self._role_id}'

    def to_dict(self):
        return {
            'username': self._username,
            'name': self._name,
            'surname': self._surname,
            'email': self._email,
            'password': self._pass_hash,
            'role': self._role_id
        }

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def email(self):
        return self._email

    @property
    def pass_hash(self):
        return self._pass_hash

    @property
    def role_id(self):
        return self._role_id

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @username.setter
    def username(self, value):
        self._username = value

    @name.setter
    def name(self, value):
        self._name = value

    @surname.setter
    def surname(self, value):
        self._surname = value

    @email.setter
    def email(self, value):
        self._email = value

    @pass_hash.setter
    def pass_hash(self, value):
        self._pass_hash = value

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
