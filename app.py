__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "1.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template,request, session,send_file
import os
import model.login as logins
import model.user as users
import model.iaxray as ia
from typing import Union
import re
########
from multiprocessing import Pool
import subprocess
import multiprocessing

########
module_name = __name__
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
__path__ = os.getcwd()
path = os.getcwd()
print(path)

# file Upload
CDSEXT   = os.path.join(path, 'cdsext')
if not os.path.isdir(CDSEXT):
    os.mkdir(CDSEXT)

GB2FASTA = os.path.join(path, 'gb2fasta')
if not os.path.isdir(GB2FASTA):
    os.mkdir(GB2FASTA)

AIPICS = os.path.join(path, 'pics')

if not os.path.isdir(AIPICS):
    os.mkdir(AIPICS)

DNATORNA = os.path.join(path, 'dnatorna')

if not os.path.isdir(DNATORNA):
    os.mkdir(DNATORNA)

DNATOPROTEIN = os.path.join(path, 'dnaprotein')

if not os.path.isdir(DNATOPROTEIN):
    os.mkdir(DNATOPROTEIN)


### ERRORS
@app.errorhandler(400)
def bad_request_error(error):
    message = "Sorry, the request was malformed."
    return render_template('error.html', message=message), 400

@app.errorhandler(401)
def unauthorized_error(error):
    message = "Sorry, you are not authorized to access this page."
    return render_template('error.html', message=message), 401

@app.errorhandler(403)
def forbidden_error(error):
    message = "Sorry, you do not have permission to access this page."
    return render_template('error.html', message=message), 403

@app.errorhandler(408)
def timeout_error(error):
    message = "Sorry, the server timed out while processing your request."
    return render_template('error.html', message=message), 408

@app.errorhandler(502)
def bad_gateway_error(error):
    message = "Sorry, there was a problem with the server's connection to another server."
    return render_template('error.html', message=message), 502

@app.errorhandler(503)
def service_unavailable_error(error):
    message = "Sorry, the server is currently unable to handle your request."
    return render_template('error.html', message=message), 503

@app.errorhandler(404)
def page_not_found(e):
    message = "Sorry, the page you requested was not found."
    return render_template('error.html', message=message), 404

@app.errorhandler(500)
def internal_server_error(e):
    message = "Sorry, something went wrong on the server."
    return render_template('error.html', message=message), 500
###

@app.route('/', methods=['GET', 'POST'])
def index():
    """Show the principal page of the app"""
    if request.method == 'POST':
        return render_template('login.html')
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Show the login form and log the user in if the credentials are correct"""
    if request.method == 'POST':
        username: str =  request.form['username']
        password: str =  request.form['password']
        resultado: Union[bool, users.User] = logins.login(username, password)
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
    """Delete the session data, this will log the user out"""
    session.pop('username', None)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Show the register page of the app """
    if request.method == 'POST':
        username: str =  request.form['username']
        name: str =  request.form['name']
        surname: str =  request.form['surname']
        email: str =  request.form['email']
        password: str =  request.form['password']
        role_id: int =  request.form['role_id']
        resultado: bool = logins.register(username, name, surname, email, password, role_id)
        if resultado:
            message = "Register successful"
            return render_template('register.html', message=message)
        else:
            message = "Register failed"
            return render_template('register.html', message=message)
    return render_template('register.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    """Show the home page of the app if the user is logged in"""
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

@app.route('/iamlr',methods=['GET', 'POST'])
def iamlr():
    """Show the image recognition page"""
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join(AIPICS, filename))
            fullroute=os.path.join(AIPICS, filename)
            solve = ia.IAML.ask(fullroute)
        return render_template('ia.html', solve=solve)
    return render_template('ia.html')

@app.route('/dnatoprotein',methods=['GET', 'POST'])
def DNA_to_protein():
    """Show the cds page"""
    if request.method == 'POST':
        file = request.files['dnaprotein']
        if file:
            filename = file.filename
            file.save(os.path.join(DNATOPROTEIN, filename))
            fullroute=os.path.join(DNATOPROTEIN, filename)
            subprocess.run(["./dna_protein",fullroute])
            new_filename = re.sub(r'\.fasta$', '_protein.fasta', filename)
        return send_file("dnaprotein/"+new_filename, as_attachment=True)
    return render_template('dna_protein.html')

@app.route('/dnatorna',methods=['GET', 'POST'])
def DNA_to_RNA():
    """Show the cds page"""
    if request.method == 'POST':
        file = request.files['dnarna']
        if file:
            filename = file.filename
            file.save(os.path.join(DNATORNA, filename))
            fullroute=os.path.join(DNATORNA, filename)
            subprocess.run(["./dna_rna",fullroute])
        return render_template('dna_rna.html')
    return render_template('dna_rna.html')

@app.route('/cdsextract',methods=['GET', 'POST'])
def cdsextract():
    """Show the cds extract page"""
    if request.method == 'POST':
        file = request.files['extractcds']
        if file:
            filename = file.filename
            file.save(os.path.join(CDSEXT, filename))
            fullroute=os.path.join(CDSEXT, filename)
            subprocess.run(["./starting",fullroute])
        return render_template('cds.html')
    return render_template('cds.html')

# Genbank to fasta 
#-------------------------------------------
@app.route('/gbtofasta',methods=['GET', 'POST'])
def gb_to_fasta():
    """Show the cds extract page"""
    if request.method == 'POST':
        file = request.files['gbfile']
        if file:
            filename = file.filename
            file.save(os.path.join(GB2FASTA, filename))
            fullroute=os.path.join(GB2FASTA, filename)
            result = subprocess.run(["./genbankToFastaV3",fullroute], stdout=subprocess.PIPE, text=True)

        return render_template('gbtofasta.html', message=result.stdout, filename=filename)
    return render_template('gbtofasta.html')

# Global aligment
#-------------------------------------------
@app.route('/globalalignment',methods=['GET', 'POST'])
def global_alignment():
    """Show the cds extract page"""
    if request.method == 'POST':
        fasta1 = request.files['fasta1']
        fasta2 = request.files['fasta2']
        if fasta1 and fasta2:
            fasta1_filename = fasta1.filename
            fasta2_filename = fasta2.filename

            fasta1.save(os.path.join(GB2FASTA, fasta1_filename))
            fasta1.save(os.path.join(GB2FASTA, fasta2_filename))

            fasta1_filepath = os.path.join(GB2FASTA, fasta1_filename)
            fasta2_filepath = os.path.join(GB2FASTA, fasta2_filename)

            subprocess.run(["./globalAligmentV2ArgsFileIn",fasta1_filepath, fasta2_filepath])

        return render_template('global_aligment.html')
    return render_template('global_aligment.html')

@app.route('/random_sequence', methods=['GET', 'POST'])
def random_sequence():
    """Show the random sequence page"""
    if request.method == 'POST':                                            
        return render_template('random_sequence.html')
    return render_template('random_sequence.html')


@app.route('/underconstruction', methods=['GET', 'POST'])
def under_construction():
    """Show the view under construction"""
    if request.method == 'POST':
        return render_template('underconstruction.html')
    return render_template('underconstruction.html')

# @app.route('/dnatorna', methods=['GET', 'POST'])
# def dnatorna():
#     """Show the dnatorna page"""
#     if request.method == 'POST':
#         sequence: str =  request.form['sequence']
#         print(sequence)
#         res = subprocess.run(["./1_team_members/luis/luis", sequence])
#         return render_template('dna_rna.html')
#     return render_template('dna_rna.html')

### Create the app
def create_app():
    return app


### START THE APP ###
if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=5000)