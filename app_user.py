from flask import Blueprint, render_template, request, session
from typing             import Union
import hashlib
import model.login as logins
import model.user as users
import model.roles as roles
import model.petition as petitiones
import model.upload as upload
import model.scripts as sc
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
            session["role_id"] = resultado.role_id
            print(f"hola {session.get('username')}")
            session['username'] = username
            return render_template('about_us.html', message=message)
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
    """Show the register page of the app
    if not logged in redirect to the login page
    if logged show the register page and create the user"""

    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET' and session.get('role_id') == 1:
        roles_list = upload.select_from("*", "role")
        roles_p_id = [sc.dict_to_role(r) for r in roles_list]
        return render_template('register.html', roles=roles_p_id)

    if request.method == 'POST'  and session.get('role_id') == 1:
        # Get the data from the form
        username: str =  request.form['username']
        name:     str =  request.form['name']
        surname:  str =  request.form['surname']
        email:    str =  request.form['email']
        password: str =  request.form['password']
        role_id:  int =  request.form['role_id']
        # Hash the password
        pass_hash =  hashlib.sha256(password.encode()).hexdigest()
        # Create the user
        user = users.User(username, name, surname, email, pass_hash, role_id)
        # Register the user
        resultado: bool = logins.register(user)
        pepe = upload.delete_petitions(user.username)
        print("pepe")
        print(pepe)
        # If the user is registered redirect to the login page else redirect to the register page
        if resultado:
            message = "Register successful"
            roles_list = upload.select_from("*", "role")
            roles_p_id = [sc.dict_to_role(r) for r in roles_list]
            return render_template('register.html', message=message,roles=roles_p_id)
        else:
            message = "Register failed"
            roles_list = upload.select_from("*", "role")
            roles_p_id = [sc.dict_to_role(r) for r in roles_list]
            return render_template('register.html', message=message,roles=roles_p_id)
    else:
        return render_template('error.html', message="Unauthorized access, only doctors can create petitions")


@user_controller.route('/edit_account', methods=['GET', 'POST'])
def edit_account():
    """Show the edit account page of the app
    if not logged in redirect to the login page
    if logged show the edit account page"""

    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        username:str = session.get('username')
        user_data: Union[bool, users.User] = logins.get_user_data_from_database(username)
        return render_template('edit_account.html', user_data=user_data)
    
    if request.method == 'POST':
        new_username:str = request.form['username']
        new_name:str = request.form['name']
        new_surname:str = request.form['surname']
        new_email:str = request.form['email']
        username:str = session.get('username')

        resultado = logins.edit(new_username, new_name, new_surname, new_email)
        if resultado:
            message:  str = "Successful edited"
            username: str = session.get('username')
            user_data: Union[bool, users.User] = logins.get_user_data_from_database(username)
            return render_template('edit_account.html', message=message, user_data=user_data)
        else:
            message = "Failed edit"
        return render_template('edit_account.html', message=message)
    
@user_controller.route('/petition_newuser', methods=['GET', 'POST'])
def petition_newuser():
    """Show the petition page of the app
    if not logged in redirect to the login page
    if logged in and admin redirect to the doctor petition page
    if logged in and user or admin redirect to the error page
    """
    if not logins.is_logged(): return render_template('login.html') # Validate session
    if request.method == 'GET' and session.get('role_id') == 2:
        admins = upload.select_from_where_table("users","role_id",1)
        admins_list = [sc.tuple_to_object(tup) for tup in admins]
        return render_template('petitions_doctor.html',admins=admins_list)
    if request.method == 'POST' and session.get('role_id') == 2:
        name = request.form["name"]
        surname = request.form["surname"]
        username = request.form["username"]
        email = request.form["email"]
        role_id = request.form["role_id"]
        admin = request.form["admins"]
        pet = petitiones.Petition(admin,username,name, surname, email, role_id)
        done = logins.petition_user(pet)
        print("SSSss")
        print(done)
        if done == True:
            admins = upload.select_from_where_table("users","role_id",1)
            admins_list = [sc.tuple_to_object(tup) for tup in admins]
            return render_template('petitions_doctor.html',admins=admins_list,message="Petition successful")
        else:
            admins = upload.select_from_where_table("users","role_id",1)
            admins_list = [sc.tuple_to_object(tup) for tup in admins]
            return render_template('petitions_doctor.html',admins=admins_list,message="Error, try again with different username")

    else:
        return render_template('error.html', message="Unauthorized access, only doctors can create petitions")
@user_controller.route('/list_petitions', methods=['GET', 'POST'])
def list_petitions():
    """Show the list of petitions page of the app 
    if not logged in redirect to the login page
    if logged in and admin redirect to the admin page
    if logged in and user or doctor redirect to the error page"""
    if not logins.is_logged(): return render_template('login.html') # Validate session
    if request.method == 'GET' and session.get('role_id') == 1:
        user_name = session.get('username')
        print(user_name)
        petitions = upload.select_from_where_table("petitions","admin_petition",f"'{user_name}'")
        print(petitions)
        petition_list = [sc.tuple_to_petition(petition) for petition in petitions]
        return render_template('admin_list_petitions.html', petitions=petition_list)
    if request.method == 'POST' and session.get('role_id') == 1:
        petition_user = request.form['petition_user']
        petitions = upload.select_from_where_table("petitions","username",f"'{petition_user}'")
        pet = [sc.tuple_to_petition(pet) for pet in petitions]
        petition_send = pet[0] 
        roles_list = upload.select_from("*", "role")
        roles_p_id = [sc.dict_to_role(r) for r in roles_list]
        return render_template('register_from_petition.html',petition=petition_send,roles=roles_p_id)
        # pass
    else:
        return render_template('error.html', message="Unauthorized access, only doctors can create petitions")