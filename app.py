__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "1.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template,request
import os
import mysql.connector
from flask_sqlalchemy import SQLAlchemy


module_name = __name__
app = Flask(__name__)

__path__ = os.getcwd()

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

        # Creamos un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Verificamos si el usuario y la contraseña son correctos
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        resultado = cursor.fetchone()
        # user = get_user(username, password)

        if resultado:
            print(resultado)
            # login_user(user)
            message = "Login successful"
            return render_template('index.html')
        else:
            return "Usuario o contraseña incorrectos"


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

@app.route('under_construction', methods=['GET', 'POST'])
def under_construction():
    if request.method == 'POST':
        return render_template('under_construction.html')
    return render_template('under_construction.html')

def create_app():
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=5000)