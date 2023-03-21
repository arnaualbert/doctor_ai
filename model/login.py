import mysql.connector
import model.user as user
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="doctor_ai"
)


def login(username, password):
        #create a cursor
        cursor = conexion.cursor()
        # Verify if the user is correct
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        # resultado = cursor.fetchall()
        resultado = cursor.fetchone()
        u = user.User(*resultado)
        return u
