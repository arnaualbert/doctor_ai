__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "1.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template,request, session
import os
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import model.login as logins

module_name = __name__
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
__path__ = os.getcwd()

# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="doctor_ai"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('login.html')
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username =  request.form['username']
        password =  request.form['password']
        resultado = logins.login(username, password)
        if resultado:
            print(resultado)
            message = "Login successful"
            session['username'] = resultado.username
            print(f"hola {session.get('username')}")
            session['username'] = username
            return render_template('index.html')
        else:
            return render_template("login.html")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username =  request.form['username']
        name =  request.form['name']
        surname =  request.form['surname']
        email =  request.form['email']
        password =  request.form['password']
        role_id =  request.form['role_id']
        resultado = logins.register(username, name, surname, email, password, role_id)
        if resultado:
            print(resultado)
            message = "Register successful"
            return render_template('index.html')
        else:
            return render_template("register.html")
    return render_template('register.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if session.get('username')  != None:
            return render_template('index.html')
        else:
            return render_template('login.html')

    if request.method == 'GET'and session.get('username')  != None:
        if session.get('username')  != None:
            return render_template('index.html')
        else:
            return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    name = request.form['name']
    surname = request.form['surname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    pass

@app.route('/iamlr',methods=['GET', 'POST'])
def iamlr():
    if request.method == 'POST':
        return render_template('ia.html')
    return render_template('ia.html')


@app.route('/underconstruction', methods=['GET', 'POST'])
def under_construction():
    if request.method == 'POST':
        return render_template('underconstruction.html')
    return render_template('underconstruction.html')

def create_app():
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=5000)