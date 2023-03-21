__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "1.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template,request,redirect,url_for
import os

module_name = __name__
app = Flask(__name__)

__path__ = os.getcwd()

@app.route('/', methods=['GET', 'POST'])
def index():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    pass

def create_app():
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=5000)