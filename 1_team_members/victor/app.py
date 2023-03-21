from flask       import Flask, render_template, request, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

import mysql.connector
import models.User


class User(UserMixin):

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(id):
        return User(id)

app = Flask(__name__)
app.secret_key = 'secret_key'

# Creamos la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="vic",
    password="123qwe",
    database="user-uf4"
)


# login_manager = LoginManager()
# login_manager.init_app(app)

# # Función para obtener un usuario de la base de datos
# def get_user(username, password):
#     cursor = mysql.cursor()
#     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))

#     data = cursor.fetchone()
#     if data is None:
#         return None
#     else:
#         user = User(id=data[0], username=data[1], password=data[2])
#         return user



# @app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
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
            return render_template('logged.html', message=message)
        else:
            return "Usuario o contraseña incorrectos"


    return render_template('login.html')



@app.route('/register',method=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form('name')
        surname = request.form('surname')
        username = request.form('username')
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)