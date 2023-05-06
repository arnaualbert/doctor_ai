from flask import Blueprint, render_template, request, session
from typing             import Union
import hashlib
import model.login as logins
import model.user as users
import model.upload as upload

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/login', methods=['GET', 'POST'])
def login():
    """Show the login form and log the user in if the credentials are correct"""
    if request.method == 'GET':
        return render_template('index.html', message=message)

    if request.method == 'POST':
        # Get the data from the form
        username: str =  request.form['username']
        password: str =  request.form['password']
        resultado: Union[bool, users.User] = logins.login(username, password)
        # If the credentials are correct log the user in and redirect to the home page else redirect to the login page
        if resultado:
            print(resultado)
            message = "Login successful"
            session['username'] = resultado.username
            session["user_id"] = resultado.id
            print(f"hola {session.get('username')}")
            session['username'] = username
            return render_template('index.html', message=message)
        else:
            message = 'Login failed'
            return render_template("login.html", message=message)

@user_controller.route('/logout')
def logout():
    """Delete the session data, this will log the user out"""
    session.pop('username', None)
    return render_template('login.html')


@user_controller.route('/register', methods=['GET', 'POST'])
def register():
    """Show the register page of the app """
    if request.method == 'GET':
        roles = (upload.select_from('role_name', 'role'))
        roles_ids = (upload.select_from('id', 'role'))
        roles_list = [(r['role_name']) for r in roles]
        roles_id_list = [(r['id']) for r in roles_ids]
        roles_p_id = list(zip(roles_list, roles_id_list))

        return render_template('register.html', roles=roles_p_id)

    if request.method == 'POST':
        # Get the data from the form
        username: str =  request.form['username']
        name: str =  request.form['name']
        surname: str =  request.form['surname']
        email: str =  request.form['email']
        password: str =  request.form['password']
        role_id: int =  request.form['role_id']
        # Hash the password
        pass_hash =  hashlib.sha256(password.encode()).hexdigest()
        # Create the user
        user = users.User(username, name, surname, email, pass_hash, role_id)
        # Register the user
        resultado: bool = logins.register(user)
        # If the user is registered redirect to the login page else redirect to the register page
        if resultado:
            message = "Register successful"
            return render_template('register.html', message=message)
        else:
            message = "Register failed"
            return render_template('register.html', message=message)

    return render_template('register.html')

@user_controller.route('/edit_account', methods=['GET', 'POST'])
def edit_account():
    """Show the edit account page of the app """
    username:str = session.get('username')
    user_data: Union[bool, users.User] = logins.get_user_data_from_database(username)
    name:str = user_data.name
    surname:str = user_data.surname
    email:str = user_data.email
    if request.method == 'POST':
        new_username:str = request.form['username']
        new_name:str = request.form['name']
        new_surname:str = request.form['surname']
        new_email:str = request.form['email']

        resultado = logins.edit(new_username, new_name, new_surname, new_email)
        if resultado:
            message = "Successful edited"
            return render_template('edit_account.html', message=message,name=new_name,surname=new_surname, username=new_username, email=new_email)
        else:
            message = "Failed edit"
        return render_template('edit_account.html', message=message)
    
    return render_template('edit_account.html', name=name,surname=surname, username=username, email=email)