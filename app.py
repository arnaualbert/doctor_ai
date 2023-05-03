__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "2.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template, request, session,send_file, redirect, url_for
import os
import model.login as logins
import model.user as users
import model.iaxray as ia
import model.upload as upload
from typing import Union
from datetime import datetime
from pathlib import Path
import shutil
import glob
import re
from celery import Celery, Task
from multiprocessing import Process
import model.validators as validate
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import model.scripts as sc
executor = ThreadPoolExecutor(5)
########
from multiprocessing import Pool
from random import *
import subprocess
import multiprocessing
import hashlib

########
module_name = __name__
app = Flask(__name__)
####NO TOCAR
###################
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
__path__ = os.getcwd()
path = os.getcwd()
print(path)


TOOLS_PATH =  os.path.join(path, 'tools')
if not os.path.isdir(TOOLS_PATH):
    os.mkdir(TOOLS_PATH)
    
# file Upload
CDSEXT   = os.path.join(path, 'cdsext')
if not os.path.isdir(CDSEXT):
    os.mkdir(CDSEXT)

GB2FASTA = os.path.join(path, 'gb2fasta')
if not os.path.isdir(GB2FASTA):
    os.mkdir(GB2FASTA)

GBLALIGN = os.path.join(path, 'globalAlign')
if not os.path.isdir(GBLALIGN):
    os.mkdir(GBLALIGN)

LCLALIGN = os.path.join(path, 'localAlign')
if not os.path.isdir(LCLALIGN):
    os.mkdir(LCLALIGN)

AIPICS = os.path.join(path, 'pics')

if not os.path.isdir(AIPICS):
    os.mkdir(AIPICS)

DNATORNA = os.path.join(path, 'dnatorna')

if not os.path.isdir(DNATORNA):
    os.mkdir(DNATORNA)

DNATOPROTEIN = os.path.join(path, 'dnaprotein')

if not os.path.isdir(DNATOPROTEIN):
    os.mkdir(DNATOPROTEIN)

RANDOM_SEQ = os.path.join(path, 'randomseqs')

if not os.path.isdir(RANDOM_SEQ):
    os.mkdir(RANDOM_SEQ)

SPLIT_FASTA = os.path.join(path, 'splits')

if not os.path.isdir(SPLIT_FASTA):
    os.mkdir(SPLIT_FASTA)

COMPLEMENTARY_FASTA = os.path.join(path, 'complementary_one')

if not os.path.isdir(COMPLEMENTARY_FASTA):
    os.mkdir(COMPLEMENTARY_FASTA)

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
        # Get the data from the form
        username: str =  request.form['username']
        name: str =  request.form['name']
        surname: str =  request.form['surname']
        email: str =  request.form['email']
        password: str =  request.form['password']
        role_id: int =  request.form['role_id']
        pass_hash =  hashlib.sha256(password.encode()).hexdigest()
        print(role_id)
        user = users.User(username, name, surname, email, pass_hash, role_id)
        # resultado: bool = logins.register(username, name, surname, email, password, role_id)
        resultado: bool = logins.register(user)
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
    if request.method == 'POST' and session.get('username') != None:
        return render_template('index.html')
    elif request.method == 'GET'and session.get('username')  != None:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/iamlr',methods=['GET', 'POST'])
def iamlr():
    """Show the image recognition page"""
    if session.get('username') and request.method == 'POST':
        # Get the data from the form
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join(AIPICS, filename))
            fullroute=os.path.join(AIPICS, filename)
            # Execute the image recognition program
            solve = ia.IAML.ask(fullroute)
        return render_template('ia.html', solve=solve)
    elif session.get('username') and request.method =='GET':
        return render_template('ia.html')
    else:
        return render_template('login.html')

@app.route('/dnatoprotein',methods=['GET', 'POST'])
def DNA_to_protein():
    """Show the cds page"""
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnaprotein']
        if file:
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            file.save(os.path.join(DNATOPROTEIN, filename))
            fullroute=os.path.join(DNATOPROTEIN, filename)
            # Excecute the dna to protein program
            if fullroute.endswith('.fasta'):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_protein, args=(fullroute,filename,user_id,id))
                daemon = daemon.start()
            return render_template('dna_protein.html')        
    return render_template('dna_protein.html')

    
@app.route('/dnatorna',methods=['GET', 'POST'])
def DNA_to_RNA():
    """Show the cds page"""
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnarna']
        if file:
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            file.save(os.path.join(DNATORNA, filename))
            fullroute=os.path.join(DNATORNA, filename)
            # Excecute the dna to rna program
            if fullroute.endswith('.fasta'):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_rna, args=(fullroute,filename,user_id,id))
                daemon = daemon.start()
        return render_template('dna_rna.html')
    return render_template('dna_rna.html')


@app.route('/cdsextract',methods=['GET', 'POST'])
def cdsextract():
    """Show the cds extract page"""
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['extractcds']
        if file:
            filename = file.filename
            file.save(os.path.join(CDSEXT, filename))
            fullroute=os.path.join(CDSEXT, filename)
            # Excecute the cds extract program
            if file.filename.endswith('.gb'):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.cdsextract_task, args=(fullroute,user_id))
                daemon = daemon.start()
                return render_template('cds.html')
    return render_template('cds.html')

# Genbank to fasta 
#-------------------------------------------

@app.route('/gbtofasta',methods=['GET', 'POST'])
def gb_to_fasta():
    """Show the cds extract page"""
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['gbfile']
        if file:
            filename = file.filename
            file.save(os.path.join(GB2FASTA, filename))
            fullroute=os.path.join(GB2FASTA, filename)
            # Excecute the genbank to fasta program
            if file.filename.endswith('.gb'):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.genbank_to_fasta, args=(fullroute,user_id))
                daemon = daemon.start()
                return render_template('gbtofasta.html')
    return render_template('gbtofasta.html')

# Global aligment
#-------------------------------------------
@app.route('/globalalignment',methods=['GET', 'POST'])
def global_alignment():
    """Gloabal alignment tool
        - In this verison deletes the result form server
    """

    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1']
        fasta2 = request.files['fasta2']

        match    = request.form['match']
        mismatch = request.form['mismatch']
        gap      = request.form['gap']
        if fasta1 and fasta2:
            fasta1_filename = fasta1.filename
            fasta2_filename = fasta2.filename

            fasta1.save(os.path.join(GBLALIGN, fasta1_filename))
            fasta2.save(os.path.join(GBLALIGN, fasta2_filename))

            fasta1_filepath = os.path.join(GBLALIGN, fasta1_filename)
            fasta2_filepath = os.path.join(GBLALIGN, fasta2_filename)

            # Execute the global aligment program
            output = subprocess.run(["./global_aligment_last",fasta1_filepath, fasta2_filepath, match, mismatch, gap], capture_output=True)
            print(output)

            if len(output.stdout) > 0:
                message = 'Data file format is not correct.'
                return render_template('global_aligment.html', message=message)
            else:   
                result_id: str = str(randint(1,9999999))
                user_id:   str = session.get('user_id')

                file_up:      str = "global_alignment_result.txt"
                new_filename: str = re.sub(r'\.txt$',result_id+'.txt', file_up)
                print(new_filename)
                os.rename('./'+file_up, new_filename)
                # shutil.move(path+'/'+new_filename, './globalAlign/results/')
                # new_filename_path = './globalAlign/results/'+new_filename
                # print(new_filename_path)
                query = "global_alignment"
                upload.upload_results_global(result_id,query,new_filename,user_id)
                # if (fasta1_filepath and fasta2_filepath):
                #     os.remove(fasta1_filepath)
                #     os.remove(fasta2_filepath)
                response = send_file(new_filename,as_attachment=True)
                # os.remove(new_filename)
                return response

        if not fasta1 or not fasta2:
            message = "Please upload both files"
            return render_template('global_aligment.html', message=message)

    return render_template('global_aligment.html')

#Local aligment
# #-------------------------------------------
@app.route('/localalignment',methods=['GET', 'POST'])
def local_alignment():
    """Show the local alignment page"""
    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1local']
        fasta2 = request.files['fasta2local']
        match = request.form['match']
        mismatch = request.form['mismatch']
        gap = request.form['gap']
        if fasta1 and fasta2:
            fasta1_filename = fasta1.filename
            fasta2_filename = fasta2.filename
            fasta1.save(os.path.join(LCLALIGN, fasta1_filename))
            fasta2.save(os.path.join(LCLALIGN, fasta2_filename))
            fasta1_filepath = os.path.join(LCLALIGN, fasta1_filename)
            fasta2_filepath = os.path.join(LCLALIGN, fasta2_filename)
            user_id = session.get('user_id')
            daemon = Thread(target=sc.local, args=(fasta1_filepath, fasta2_filepath, match, mismatch, gap,user_id), daemon=True)
            daemon.start()
        return render_template('local_aligment.html')

    return render_template('local_aligment.html')

@app.route('/random_sequence', methods=['GET', 'POST'])
def random_sequence():
    """Show the random sequence page"""
    if request.method == 'POST':
        # Get the data from the form
        number = request.form['number']
        number_int = int(number)

        if number_int <= 0 or number.isnumeric() == False:
            return render_template('random_sequence.html', message="Number must be greater than 0")
        else:
            user_id = session.get('user_id')
            # daemon = Thread(target=random_sequence_task, args=(number,user_id),daemon=True)
            daemon = Thread(target=sc.random_sequence_task, args=(number,user_id),daemon=True)
            daemon.start()
            return render_template('random_sequence.html', message="Your random sequence is in progress, it's going to be stored in your history")
    return render_template('random_sequence.html')

def is_fasta_file_with_only_ATGC(filename):
    if filename.endswith('.fasta'):
        with open(filename) as f:
            first_line = f.readline().strip()
            if not first_line.startswith('>') or first_line.startswith(';'):
                return False
            for line in f:
                if any(letter not in 'ATGC' for letter in line.strip()):
                    return False
            return True
    else:
        return False


def read_fasta_file(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension not in ['.fasta', '.fa']:
        # raise ValueError("File must be in .fasta or .fa format")
        return False
    else:
        return True


def count_letters_in_file(filename):
    with open(filename, "r") as file:
        next(file)
        count = 0
        for line in file:
            count += len(line.strip())

    return count

@app.route('/split_fasta', methods=['GET', 'POST'])
def split_fasta():
    ""
    if request.method == 'POST':
        fasta = request.files["split"]
        start = request.form['start']
        end = request.form['end']
        fasta_ext = fasta.filename
        fasta.save(os.path.join(SPLIT_FASTA,fasta_ext))
        full_path = os.path.join(SPLIT_FASTA,fasta_ext)
        # if fasta_ext.endswith(".fasta") and int(start)>0 and int(end)>0 and start.isnumeric() and end.isnumeric() and int(start)<=count_letters_in_file(full_path) and int(end)<=count_letters_in_file(full_path):
        # if is_fasta_file_with_only_ATGC(full_path) and int(start)>0 and int(end)>0 and start.isnumeric() and end.isnumeric() and int(start)<=count_letters_in_file(full_path) and int(end)<=count_letters_in_file(full_path):
        if validate.validate_split_fasta(full_path,start,end):
            daemon = Thread(target=sc.split_fasta_task, args=(full_path,session.get('user_id'),start,end),daemon=True)
            daemon.start()
            return render_template('split.html', message="Doing the job")
        else:
            # os.remove(full_path)
            return render_template('split.html', message="File must be in .fasta format and inputs must be numbers bigger tha 0")
    return render_template('split.html')


@app.route("/complementary", methods=['GET', 'POST'])
def complementary():
    if request.method == 'POST':
        fasta = request.files["complementary"]
        fasta_ext = fasta.filename
        fasta.save(os.path.join(COMPLEMENTARY_FASTA,fasta_ext))
        full_path = os.path.join(COMPLEMENTARY_FASTA,fasta_ext)
        if fasta_ext.endswith(".fasta"):
            deamon = Thread(target=sc.complementary_task, args=(full_path,session.get('user_id')),daemon=True)
            deamon.start()
            return render_template('complementary.html', message="Doing the job")
    return render_template('complementary.html')



@app.route("/blast",methods=['GET', 'POST'])
def blast():
    if request.method == 'POST':
        return render_template('blast.html')
    return render_template('blast.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    """Show the history page"""
    if request.method == 'GET':
        # Show the history
        user_id = session.get('user_id')
        list_of_results = upload.download_results(user_id)
        results = list_of_results
        return render_template('history.html',results=results)
    return render_template('history.html')


@app.route('/history_query', methods=['GET', 'POST'])
def history_query():
    """Show the history page"""
    if request.method == 'POST':
        # Show the history
        user_id = session.get('user_id')
        tool = request.form['query_order']
        list_of_results = upload.select_by_tool(tool,user_id)
        results = list_of_results
        return render_template('history.html',results=results)
    return render_template('history.html')


@app.route('/underconstruction', methods=['GET', 'POST'])
def under_construction():
    """Show the view under construction"""
    if request.method == 'POST':
        return render_template('underconstruction.html')
    return render_template('underconstruction.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    """Download a file"""
    return send_file(filename, as_attachment=True)

### Create the app
def create_app():
    return app

@app.route('/delete-row/<int:id>', methods=['DELETE'])
def eliminar_fila(id):
    if request.method == "DELETE":
        upload.delete_job(id)

    return redirect(url_for('history'))

### START THE APP ###
if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=8080)
