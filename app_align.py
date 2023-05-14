from flask import Blueprint, render_template, request, session, send_file
from typing             import Union
import hashlib
import model.upload as upload
import subprocess
from random             import *
from threading          import Thread
import model.scripts    as sc
import model.login      as logins
import model.validators as validate
import os
import re
align_controller = Blueprint('align_controller', __name__)
__path__ = os.getcwd()
path = os.getcwd()
print(path)


def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)

GBLALIGN = os.path.join(path, 'globalAlign')
create_directory(GBLALIGN)

LCLALIGN = os.path.join(path, 'localAlign')
create_directory(LCLALIGN)



# Global aligment
#-------------------------------------------
@align_controller.route('/globalalignment',methods=['GET', 'POST'])
def global_alignment():
    """Gloabal alignment tool
        - In this verison deletes the result form server
    """
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('global_aligment.html')
    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1']
        fasta2 = request.files['fasta2']

        match    = request.form['match']
        mismatch = request.form['mismatch']
        gap      = request.form['gap']
        user_filename = request.form['user_filename']
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

                os.rename('./'+file_up, new_filename)
                query = "global_alignment"
                upload.upload_results_global(result_id,query,new_filename,user_id)
                response = send_file(new_filename,as_attachment=True)
                # os.remove(new_filename)
                return response

        if not fasta1 or not fasta2:
            message = "Please upload both files"
            return render_template('global_aligment.html', message=message)

#Local aligment
# #-------------------------------------------
@align_controller.route('/localalignment',methods=['GET', 'POST'])
def local_alignment():
    """Show the local alignment page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('local_aligment.html')
    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1local']
        fasta2 = request.files['fasta2local']
        match = request.form['match']
        mismatch = request.form['mismatch']
        gap = request.form['gap']
        gapLeft = request.form['gapLeft']
        gapUp = request.form['gapUp']
        user_filename = request.form['user_filename']
        fasta1local = sc.save_fasta_file(fasta1, LCLALIGN)
        fasta2local = sc.save_fasta_file(fasta2, LCLALIGN)
        if validate.validate_local_aligment(fasta1local, fasta2local, match, mismatch, gap,gapLeft,gapUp) == True:
            print("hola")
            user_id = session.get('user_id')
            daemon = Thread(target=sc.local, args=(fasta1local, fasta2local, match, mismatch, gap,gapLeft,gapUp,user_id,user_filename), daemon=True)
            daemon.start()
            # return "running"
            return render_template('local_aligment.html')
        else:
            return render_template('local_aligment.html')
        
#Blosum Local aligment
# #-------------------------------------------
@align_controller.route('/blosum_local',methods=['GET', 'POST'])
def blosum_local_alignment():
    """Show the blosum local alignment page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('blosum_local.html')
    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1local']
        fasta2 = request.files['fasta2local']
        gap = request.form['gap']
        gap_extend = request.form['gap_extend']

        user_filename = request.form['user_filename']
        fasta1local = sc.save_fasta_file(fasta1, LCLALIGN)
        fasta2local = sc.save_fasta_file(fasta2, LCLALIGN)
        if validate.validate_blosum_local_aligment(fasta1local, fasta2local,gap,gap_extend) == True:
            print("hola")
            user_id = session.get('user_id')
            daemon = Thread(target=sc.blosum_local, args=(fasta1local, fasta2local,gap,gap_extend,user_id,user_filename), daemon=True)
            daemon.start()
            # return "running"
            return render_template('blosum_local.html')
        else:
            return render_template('blosum_local.html')
        

@align_controller.route('/blosum_global',methods=['GET', 'POST'])
def blosum_global_alignment():
    """Show the blosum local alignment page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET':
        return render_template('blosum_global.html')
    if request.method == 'POST':
        # Get the data from the form
        fasta1 = request.files['fasta1local']
        fasta2 = request.files['fasta2local']
        gap = request.form['gap']
        gap_extend = request.form['gap_extend']

        user_filename = request.form['user_filename']
        fasta1local = sc.save_fasta_file(fasta1, LCLALIGN)
        fasta2local = sc.save_fasta_file(fasta2, LCLALIGN)
        if validate.validate_blosum_local_aligment(fasta1local, fasta2local,gap,gap_extend) == True:
            print("hola")
            user_id = session.get('user_id')
            daemon = Thread(target=sc.blosum_global, args=(fasta1local, fasta2local,gap,gap_extend,user_id,user_filename), daemon=True)
            daemon.start()
            # return "running"
            return render_template('blosum_global.html')
        else:
            return render_template('blosum_global.html')