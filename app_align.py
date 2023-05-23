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
    # Validate session
    if not logins.is_logged(): return render_template('login.html')

    # GET action
    if request.method == 'GET':  
        return render_template('global_aligment.html')

    # POST action
    if request.method == 'POST': # POST action
        # Get the data from the form
        fasta1 = request.files['fasta1']
        fasta2 = request.files['fasta2']

        match    = request.form['match']
        mismatch = request.form['mismatch']
        gap      = request.form['gap']

        user_filename = request.form['user_filename']

        # Get the fastas filepath from the server
        fasta1_filepath = sc.save_fasta_file(fasta1, GBLALIGN)
        fasta2_filepath = sc.save_fasta_file(fasta2, GBLALIGN)
        print(fasta1_filepath)
        # Validate the form 
        are_fasta1 = fasta1.filename != ""
        are_fasta2 = fasta2.filename != ""
        are_match = match != ""
        are_mismatch = mismatch != ""
        are_gap = gap != ""
        are_user_filename = user_filename != ""
        if are_fasta1 == True and are_fasta2 == True and are_match == True and are_mismatch == True and are_gap == True and are_user_filename == True:
            if validate.validate_GA_form(fasta1_filepath, fasta2_filepath, match, mismatch, gap) and user_filename:  

                # Execute the global aligment program
                user_id = session.get('user_id')
                daemon = Thread(target=sc.run_global_align, args=(fasta1_filepath, fasta2_filepath, match, mismatch, gap,user_id,user_filename), daemon=True)
                daemon.start()
                # result_id: str = str(randint(1,9999999))
                # user_id:   str = session.get('user_id')

                # file_up:      str = "global_alignment_result.txt"
                # new_filename: str = re.sub(r'\.txt$',result_id+'.txt', file_up)

                # os.rename('./'+file_up, new_filename)
                # query = "global_alignment"
                # upload.upload_results_global(result_id,query,new_filename,user_id)
                # response = send_file(new_filename,as_attachment=True)
                # os.remove(new_filename)
                message = 'Global alignment in process...'
                return render_template('global_aligment.html', message=message)
            else:
                message = "The fastas file does not have the correct format"
                return render_template('global_aligment.html', message=message)
        else:
            message = "Please fill all the fields"
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
        print("ASD")
        fasta1local = sc.save_fasta_file(fasta1, LCLALIGN)
        fasta2local = sc.save_fasta_file(fasta2, LCLALIGN)
        are_fasta1 = fasta1.filename != ''
        are_fasta2 = fasta2.filename != ''
        are_match = match != ''
        are_mismatch = mismatch != ''
        are_gap = gap != ''
        are_gapLeft = gapLeft != ''
        are_gapUp = gapUp != ''
        are_user_filename = user_filename != ''
        if are_fasta1 == True and are_fasta2 == True and are_match == True and are_mismatch == True and are_gap == True and are_gapLeft == True and are_gapUp == True and are_user_filename == True:
            if validate.validate_local_aligment(fasta1local, fasta2local, match, mismatch, gap,gapLeft,gapUp) == True:
                print("hola")
                user_id = session.get('user_id')
                daemon = Thread(target=sc.local, args=(fasta1local, fasta2local, match, mismatch, gap,gapLeft,gapUp,user_id,user_filename), daemon=True)
                daemon.start()
                # return "running"
                return render_template('local_aligment.html',message="Running")
            else:
                message = validate.validate_local_aligment(fasta1local, fasta2local, match, mismatch, gap,gapLeft,gapUp)
                os.remove(fasta1local)
                os.remove(fasta2local)
                return render_template('local_aligment.html',message=message)
        else:
            message = "all fields are required"
            return render_template('local_aligment.html',message=message)
            # return render_template('local_aligment.html',message="Please fill all the fields with the correct format")
        
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
        if validate.validate_blosum_local_aligment(fasta1local, fasta2local,gap,gap_extend) == True and validate.check_mime_type(fasta1local) == "text/plain" and validate.check_mime_type(fasta2local) == "text/plain":
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