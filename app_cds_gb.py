from flask import Blueprint, render_template, request, session
from typing             import Union
import hashlib
from threading          import Thread
import model.scripts    as sc
import model.login      as logins
import model.validators as validate

import os

from random             import *

cds_gb_controller = Blueprint('cds_gb_controller', __name__)

def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)

__path__ = os.getcwd()
path = os.getcwd()
print(path)


CDSEXT = os.path.join(path, 'cdsext')
create_directory(CDSEXT)

GB2FASTA = os.path.join(path, 'gb2fasta')
create_directory(GB2FASTA)


@cds_gb_controller.route('/cdsextract',methods=['GET', 'POST'])
def cdsextract():
    """Show the cds extract page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET': 
        return render_template('cds.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['extractcds']
        user_filename = request.form['user_filename']
        if file:
            # Excecute the cds extract program
            fullroute=sc.save_fasta_file(file,CDSEXT)
            if validate.is_genbank(fullroute) == True:
                user_id = session.get('user_id')
                daemon: Thread = Thread(target=sc.cdsextract_task, args=(fullroute,user_id,user_filename))
                daemon.start()
                message = "Running..."
                info    = "Go to history to see the result"
                return render_template('cds.html', message=message, info=info)
            else:
                if validate.is_genbank(fullroute) != True:
                    message = validate.is_genbank(fullroute)
                    return render_template('cds.html',err_msg=message)
                err_msg = validate.is_genbank(fullroute)
                return render_template('cds.html', err_msg=err_msg)
                
    return render_template('cds.html')

# Genbank to fasta 
#-------------------------------------------

@cds_gb_controller.route('/gbtofasta',methods=['GET', 'POST'])
def gb_to_fasta():
    """Show the cds extract page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('gbtofasta.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['gbfile']
        user_filename = request.form['user_filename']
        are_file = file.filename != ''
        are_user_filename = user_filename != ''
        if are_file == True and are_user_filename == True:
            if user_filename:
                filename = file.filename
                file.save(os.path.join(GB2FASTA, filename))
                fullroute = os.path.join(GB2FASTA, filename)
                # Excecute the genbank to fasta program
                validate_genbank: Union[str, bool] = validate.is_genbank(fullroute)
                if validate_genbank == True and validate.check_mime_type(fullroute) == "text/plain":
                    user_id = session.get('user_id')
                    daemon = Thread(target=sc.genbank_to_fasta, args=(fullroute,user_id,user_filename))
                    daemon = daemon.start()
                    message = "Running..."
                    info    = "Go to history to see the result"
                    return render_template('gbtofasta.html', message=message, info=info)
                else: 
                    if validate.is_genbank(fullroute) != True:
                        err_msg = validate.is_genbank(fullroute)
                        return render_template('gbtofasta.html',err_msg=err_msg)
                    else:
                        err_msg = "File don't have GenBank format"
                        return render_template('gbtofasta.html', err_msg=err_msg)
            else:
                err_msg = "Please put a filename for the result"
                return render_template('gbtofasta.html', err_msg=err_msg)
        else:
            err_msg = "Please upload a file"
            return render_template('gbtofasta.html', err_msg=err_msg)