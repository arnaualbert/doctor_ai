__authors__ = "Arnau Albert, Vicor Piñana, Alex Varela, Luis Cardenete"
__credits__ = ["Arnau Albert", "Vicor Piñana", "Alex Varela","Luis Cardenete"]
__version__ = "2.0"
__maintainer__ = "Doctor AI"
__status__ = "Production"

"""
This module is used to serve the backend of the application
"""

# Imports of the app
from flask import Flask, render_template, request, session,send_file
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

########
from multiprocessing import Pool
from random import *
import subprocess
import multiprocessing

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
        # Get the data from the form
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join(AIPICS, filename))
            fullroute=os.path.join(AIPICS, filename)
            # Execute the image recognition program
            solve = ia.IAML.ask(fullroute)
        return render_template('ia.html', solve=solve)
    return render_template('ia.html')

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
            subprocess.run(["./dna_protein",fullroute])
            new_filename = re.sub(r'\.fasta$', '_protein.fasta', filename)
            file_up = "dnaprotein/"+new_filename
            user_id = session.get('user_id')
            query = "dnaprotein"
            upload.upload_results(id,query,file_up,user_id)
            ###NEW
            response = send_file("dnaprotein/"+new_filename, as_attachment=True)
            os.remove("dnaprotein/"+new_filename)
            os.remove(fullroute)
            ####
        # return send_file("dnaprotein/"+new_filename, as_attachment=True)
        return response
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
            subprocess.run(["./dna_rna",fullroute])
            new_filename = re.sub(r'\.fasta$', '_modified.fasta', filename)
            file_up = "dnatorna/"+new_filename
            user_id = session.get('user_id')
            query = "dna_to_rna"
            upload.upload_results(id,query,file_up,user_id)
            ###NEW####
            response = send_file("dnatorna/"+new_filename, as_attachment=True)
            os.remove(new_filename)
        # return send_file("dnatorna/"+new_filename, as_attachment=True)
        return response
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
            subprocess.run(["./extract_cds",fullroute])
            id = randint(1,9999999)
            ids = str(id)
            file_up = Path('resultado.fasta')
            new_filename = Path(ids+'resultado.txt')
            asd = file_up.rename(new_filename)
            user_id = session.get('user_id')
            query = "cds_extract"
            upload.upload_results(id,query,asd,user_id)                         
        return send_file(asd,as_attachment=True)
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
            result = subprocess.run(["./genbankToFastaV3",fullroute], stdout=subprocess.PIPE, text=True)
            id = randint(1,9999999)
            ids = str(id)
            file_up = Path('gb_to_fasta.fasta')
            new_filename = Path(ids+'gb_to_fasta.fasta')
            asd = file_up.rename(new_filename)
            user_id = session.get('user_id')
            query = "gb_to_fasta"
            upload.upload_results(id,query,asd,user_id)                         
        return send_file(new_filename, as_attachment=True)
    return render_template('gbtofasta.html')

# Global aligment
#-------------------------------------------
@app.route('/globalalignment',methods=['GET', 'POST'])
def global_alignment():
    """Show the cds extract page"""

    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1']
        fasta2 = request.files['fasta2']

        if fasta1 and fasta2:
            fasta1_filename = fasta1.filename
            fasta2_filename = fasta2.filename

            fasta1.save(os.path.join(GBLALIGN, fasta1_filename))
            fasta2.save(os.path.join(GBLALIGN, fasta2_filename))

            fasta1_filepath = os.path.join(GBLALIGN, fasta1_filename)
            fasta2_filepath = os.path.join(GBLALIGN, fasta2_filename)

            # Execute the global aligment program
            output = subprocess.run(["./global_aligment",fasta1_filepath, fasta2_filepath], capture_output=True)
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

                os.rename(file_up, new_filename)

                # shutil.move(path+'/'+new_filename, './globalAlign/results/')
                new_filename_path = './globalAlign/results/'+new_filename
                print(new_filename_path)
                query = "global_alignment"
                upload.upload_results(result_id,query,new_filename_path,user_id)

                if (fasta1_filepath and fasta2_filepath):
                    os.remove(fasta1_filepath)
                    os.remove(fasta2_filepath)

                return send_file(new_filename, as_attachment=True)        

        if not fasta1 or not fasta2:
            message = "Please upload both files"
            return render_template('global_aligment.html', message=message)

    return render_template('global_aligment.html')

#Local aligment
#-------------------------------------------
@app.route('/localalignment',methods=['GET', 'POST'])
def local_alignment():
    """Show the cds extract page"""
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
            # Execute the local aligment program
            subprocess.run(["./local_alignment",fasta1_filepath, fasta2_filepath, match, mismatch, gap])
            id = randint(1,9999999)
            ids = str(id)
            file_up = "alignment_result.txt"
            new_filename = re.sub(r'\.txt$',ids+'alignment_result.txt', file_up)
            os.rename(file_up, new_filename)
            user_id = session.get('user_id')
            query = "local_alignment"
            upload.upload_results(id,query,new_filename,user_id)
            return send_file(new_filename,as_attachment=True)
    return render_template('local_aligment.html')

# @app.route('/random_sequence', methods=['GET', 'POST'])
# def random_sequence():
#     """Show the random sequence page"""
#     if request.method == 'POST':    
#         # Get the data from the form  
#         number = request.form['number']
#         # Execute the random sequence program
#         subprocess.run(["./random",number])  
#         id = randint(1,9999999)
#         ids = str(id)
#         file_up = "dna.fasta"
#         new_filename = re.sub(r'\.fasta$',ids+'random.fasta', file_up)
#         os.rename(file_up, new_filename)
#         user_id = session.get('user_id')
#         query = "random_sequence"
#         upload.upload_results(id,query,new_filename,user_id)                   
#         response = send_file(new_filename,as_attachment=True)
#         # return send_file(new_filename,as_attachment=True)
#         os.remove(new_filename)
#         return response
#     return render_template('random_sequence.html')


def random_sequence_task(number, user_id):
    # Execute the random sequence program
    subprocess.run(["./random", number])
    id = randint(1, 9999999)
    ids = str(id)
    file_up = "dna.fasta"
    new_filename = re.sub(r'\.fasta$', ids+'random.fasta', file_up)
    os.rename(file_up, new_filename)
    query = "random_sequence"
    upload.upload_results(id,query,new_filename,user_id)  
    # return send_file(new_filename,as_attachment=True)
    # return response

@app.route('/random_sequence', methods=['GET', 'POST'])
def random_sequence():
    """Show the random sequence page"""
    if request.method == 'POST':
        # Get the data from the form
        number = request.form['number']
        user_id = session.get('user_id')
        # Execute the task asynchronously with multiprocessing
        p = Process(target=random_sequence_task, args=(number, user_id))
        p.start()
        # return "Task started"
        return render_template('index.html')
    return render_template('random_sequence.html')










# def random_sequence_task(number, user_id):
#     # Execute the random sequence program
#     subprocess.run(["./random", number])
#     # return send_file(new_filename,as_attachment=True)
#     # return response

# @app.route('/random_sequence', methods=['GET', 'POST'])
# def random_sequence():
#     """Show the random sequence page"""
#     if request.method == 'POST':
#         # Get the data from the form
#         number = request.form['number']
#         user_id = session.get('user_id')
#         # Execute the task asynchronously with multiprocessing
#         p = Process(target=random_sequence_task, args=(number, user_id))
#         p.start()
#         id = randint(1, 9999999)
#         ids = str(id)
#         file_up = "dna.fasta"
#         new_filename = re.sub(r'\.fasta$', ids+'random.fasta', file_up)
#         os.rename(file_up, new_filename)
#         query = "random_sequence"
#         upload.upload_results(id,query,new_filename,user_id)  
#         # return "Task started"
#         response =send_file(new_filename,as_attachment=True)

#         return render_template('index.html'), response
#     return render_template('random_sequence.html')







# import asyncio
# import aiohttp

# @app.route('/random_sequence', methods=['GET', 'POST'])
# async def random_sequence():
#     """Show the random sequence page"""
#     if request.method == 'POST':
#         # Get the data from the form
#         number = request.form['number']
        
#         # Execute the random sequence program asynchronously
#         cmd = ["./random", number]
#         proc = await asyncio.create_subprocess_exec(*cmd)
#         await proc.communicate()

#         # Rename and upload the generated file asynchronously
#         id = randint(1,9999999)
#         ids = str(id)
#         file_up = "dna.fasta"
#         new_filename = re.sub(r'\.fasta$',ids+'random.fasta', file_up)
#         os.rename(file_up, new_filename)
#         user_id = session.get('user_id')
#         query = "random_sequence"
#         await asyncio.gather(upload.upload_results(id, query, new_filename, user_id))

#         # Return the generated file asynchronously
#         async with aiohttp.ClientSession() as session:
#             async with session.get(new_filename) as resp:
#                 content = await resp.read()
#         return send_file(io.BytesIO(content), as_attachment=True, attachment_filename=new_filename)
        
#     return render_template('random_sequence.html')

# import asyncio
# import aiohttp
# import io

# @app.route('/random_sequence', methods=['GET', 'POST'])
# async def random_sequence():
#     """Show the random sequence page"""
#     if request.method == 'POST':
#         # Get the data from the form
#         number = request.form['number']
        
#         # Execute the random sequence program asynchronously
#         cmd = ["./random", number]
#         proc = await asyncio.create_subprocess_exec(*cmd)
#         await proc.communicate()

#         # Rename and upload the generated file asynchronously
#         id = randint(1,9999999)
#         ids = str(id)
#         file_up = "dna.fasta"
#         new_filename = re.sub(r'\.fasta$',ids+'random.fasta', file_up)
#         os.rename(file_up, new_filename)
#         user_id = session.get('user_id')
#         query = "random_sequence"
#         await asyncio.gather(upload.upload_results(id, query, new_filename, user_id))

#         # Return the generated file asynchronously
#         async with aiohttp.ClientSession() as session:
#             async with session.get(new_filename) as resp:
#                 content = await resp.read()

#         send_file(io.BytesIO(content), as_attachment=True, attachment_filename=new_filename)
#         return render_template('random_sequence.html')    
#     return render_template('random_sequence.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    """Show the history page"""
    if request.method == 'GET':
        # Show the history
        user_id = session.get('user_id')
        list_of_results = upload.download_results(user_id)
        print(list_of_results)
        print(type(list_of_results))
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


### START THE APP ###
if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=8080)
