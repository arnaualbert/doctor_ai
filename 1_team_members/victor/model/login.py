import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="vic",
    password="123qwe",
    database="doctor_ai"
)


def login(username, password):
        #create a cursor
        cursor = conexion.cursor()
        # Verify if the user is correct
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        resultado = cursor.fetchone()

        return resultado
