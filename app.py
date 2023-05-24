__authors__ = "Arnau Albert, Victor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Victor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "5.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app #
from flask              import Flask,Blueprint, render_template, request, session,send_file, redirect, url_for
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from threading          import Thread
from typing             import Union
from random             import *
from io                 import BytesIO
import model.dir_persist as tools_dir
import model.validators as validate
import model.scripts    as sc
import model.login      as logins
import model.user       as users
import model.iaxray     as ia
import model.upload     as upload
import subprocess
import hashlib
import os
import re
from app_user     import user_controller
from app_database import database_controller
from app_dna      import dna_controller
from app_align    import align_controller
from app_cds_gb   import cds_gb_controller
from app_chat import chat_controller
executor = ThreadPoolExecutor(5)

# Create tools directorys if not exists already #
tools_dir.create_tools_directory()

# App controller #
module_name = __name__
app = Flask(__name__)

# Blueprints #
app.register_blueprint(user_controller)
app.register_blueprint(database_controller)
app.register_blueprint(dna_controller)
app.register_blueprint(cds_gb_controller)
app.register_blueprint(align_controller)
app.register_blueprint(chat_controller)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

__path__ = os.getcwd()
path = os.getcwd()
print(path)

def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)

TOOLS_PATH = os.path.join(path, 'tools')
create_directory(TOOLS_PATH)

AIPICS = os.path.join(path, 'pics')
create_directory(AIPICS)

### ERRORS ###
@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(408)
@app.errorhandler(404)
@app.errorhandler(502)
@app.errorhandler(500)
@app.errorhandler(503)
def error_handler(error):
    error_codes = {
        400: "Sorry, the request was malformed.",
        401: "Sorry, you are not authorized to access this page.",
        403: "Sorry, you do not have permission to access this page.",
        404: "Sorry, the page you requested does not exist.",
        408: "Sorry, the server timed out while processing your request.",
        500: "Sorry, the server encountered an internal error.",
        502: "Sorry, there was a problem with the server's connection to another server.",
        503: "Sorry, the service is temporarily unavailable."
    }
    message = error_codes.get(error.code, "Sorry, an error occurred.")
    return render_template('error.html', message=message), error.code
###

@app.route('/', methods=['GET', 'POST'])
def index():
    """Show the principal page of the app"""
    if request.method == 'POST':
        return render_template('login.html')
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    """Show the home page of the app if the user is logged in"""
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    """Show the home page of the app if the user is logged in"""
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('home.html')

@app.route('/iamlr',methods=['GET', 'POST'])
def iamlr():
    """Show the image recognition page
    it returns the result of the image recognition if everything is ok
    else show an error message"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('ia.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['image']
        fullroute = sc.save_fasta_file(file,AIPICS)    
        import magic
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(fullroute)
        print(mime_type)
        model_h5 = request.form['model']
        # Execute the image recognition program
        if validate.is_image_file(fullroute):
            solve = ia.IAML.ask(fullroute,model_h5)
            if solve == 'BAD':
                isPneumo = True
                return render_template('ia.html', isPneumo=isPneumo)
            else:
                isNormal = True
                return render_template('ia.html', isNormal=isNormal)
        else:
            return render_template('ia.html', solve="It needs to be an image")



@app.route("/blast",methods=['GET', 'POST'])
def blast():
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('blast.html')
    if request.method == 'POST':
        return render_template('blast.html')
    
    return render_template('blast.html')

@app.route('/underconstruction', methods=['GET', 'POST'])
def under_construction():
    """Show the view under construction"""
    if request.method == 'POST':
        return render_template('underconstruction.html')
    return render_template('underconstruction.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    """Show the view about us"""
    if request.method == 'POST':
        return render_template('about_us.html')
    return render_template('about_us.html')



@app.route('/download_file',methods=['GET', 'POST'])
def download_file():
    """Download a file"""
    if not logins.is_logged(): return render_template('login.html')
    if request.method == 'POST':
        #Request the data
        result = "result"
        table = "results"
        filename = "user_filename"
        ident = request.form["ident"]
        # Select the file
        asd = upload.select_from_where(result,filename,table,ident)
        print(asd)
        tup = asd[0]
        file_to_download = asd[1]
        bytes_io = BytesIO(tup)
        # Send the file as an attachment
        return send_file(bytes_io,mimetype="text/plain",as_attachment=True,download_name=file_to_download)


@app.route('/delete_file',methods=['GET', 'POST'])
def delete_file():
    """Delete a file"""
    if not logins.is_logged(): return render_template('login.html')
    if request.method == 'POST':
        #Request the data
        ident = request.form["ident"]
        user_id = session.get("user_id")
        # Delete the file
        upload.delete_a_results(user_id,ident)
        list_of_results = upload.download_results(user_id)
        results = list_of_results
        return render_template('history.html',results=results)
    
### Create the app ###
def create_app():
    return app

### START THE APP ###
if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=8080)
