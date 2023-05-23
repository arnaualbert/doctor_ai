from flask import Blueprint, render_template, request, session
from typing             import Union
import hashlib
from threading          import Thread
import model.scripts    as sc
import model.login      as logins
import model.validators as validate

import os

from random             import *

dna_controller = Blueprint('dna_controller', __name__)


__path__ = os.getcwd()
path = os.getcwd()
print(path)


def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)

DNATORNA = os.path.join(path, 'dnatorna')
create_directory(DNATORNA)

DNATOPROTEIN = os.path.join(path, 'dnaprotein')
create_directory(DNATOPROTEIN)

COMPLEMENTARY_FASTA = os.path.join(path, 'complementary_one')
create_directory(COMPLEMENTARY_FASTA)

RANDOM_SEQ = os.path.join(path, 'randomseqs')
create_directory(RANDOM_SEQ)

SPLIT_FASTA = os.path.join(path, 'splits')
create_directory(SPLIT_FASTA)

REVERSE= os.path.join(path, 'reverse')
create_directory(REVERSE)


@dna_controller.route('/random_sequence', methods=['GET', 'POST'])
def random_sequence():
    """Show the random sequence page"""
    if request.method == 'POST':
        # Get the data from the form
        number = request.form['number']
        user_filename = request.form['user_filename']
        number_int = int(number)

        if number_int <= 0 or number.isnumeric() == False or user_filename == "":
            return render_template('random_sequence.html', message="Number must be greater than 0")
        else:
            user_id = session.get('user_id')
            # daemon = Thread(target=random_sequence_task, args=(number,user_id),daemon=True)
            daemon = Thread(target=sc.random_sequence_task, args=(number,user_id,user_filename),daemon=True)
            daemon.start()
            return render_template('random_sequence.html', message="Your random sequence is in progress, it's going to be stored in your history")
    return render_template('random_sequence.html')


@dna_controller.route('/dnatoprotein',methods=['GET', 'POST'])
def DNA_to_protein():
    """Show the dna to protein page"""
    if not logins.is_logged(): return render_template('login.html')
    
    if request.method == 'GET': 
        return render_template('dna_protein.html')
    
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnaprotein']
        user_filename = request.form['user_filename']
        are_file = file.filename != ""
        are_user_filename = user_filename != ""
        if are_file == True and are_user_filename == True:
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            fullroute = sc.save_fasta_file_with_id(id,file,DNATOPROTEIN)
            # Excecute the dna to protein program
            if validate.is_fasta_file_with_only_nucleotide(fullroute) and validate.check_mime_type(fullroute) == "text/plain" and user_filename != "":
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_protein, args=(fullroute,filename,user_id,id,user_filename))
                daemon = daemon.start()
                return render_template('dna_protein.html',message="Doing the job, check the history")
            else:
                if validate.is_fasta_file_with_only_nucleotide(fullroute) != True:
                    message = validate.is_fasta_file_with_only_nucleotide(fullroute)
                    return render_template('dna_protein.html',message=message)
                else:
                    return render_template('dna_protein.html',message="This is not a fasta file and all the fields are required")  
        else:
            return render_template('dna_protein.html',message="All the fields are required")

    
@dna_controller.route('/dnatorna',methods=['GET', 'POST'])
def DNA_to_RNA():
    """Show the dna to rna page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET': 
        return render_template('dna_rna.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnarna']
        user_filename = request.form['user_filename']
        are_file = file.filename != "" 
        if are_file == True and user_filename != "":
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            fullroute = sc.save_fasta_file_with_id(id,file,DNATORNA)
            if validate.is_fasta_file_with_only_nucleotide(fullroute) == True and validate.check_mime_type(fullroute) == "text/plain" and user_filename != "":
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_rna, args=(fullroute,filename,user_id,id,user_filename))
                daemon = daemon.start()
                return render_template('dna_rna.html',message="Doing the job, check the history")
            else:
                if validate.is_fasta_file_with_only_nucleotide(fullroute) != True:
                    message = validate.is_fasta_file_with_only_nucleotide(fullroute)
                    return render_template('dna_rna.html',message=message)
                else:
                    return render_template('dna_rna.html',message="All the fields are required")
        else:
            return render_template('dna_rna.html',message="All the fields are required")
   

@dna_controller.route("/complementary", methods=['GET', 'POST'])
def complementary():
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('complementary.html')
    if request.method == 'POST':
        fasta = request.files["complementary"]
        user_filename = request.form['user_filename']
        fasta_ext = fasta.filename
        fasta.save(os.path.join(COMPLEMENTARY_FASTA,fasta_ext))
        full_path = os.path.join(COMPLEMENTARY_FASTA,fasta_ext)
        are_file = fasta.filename != "" 
        are_user_filename = user_filename != ""
        if are_file == True and are_user_filename == True:
            if validate.is_fasta_file_with_only_nucleotide(full_path) == True and validate.check_mime_type(full_path) == "text/plain" and user_filename != "":
                deamon = Thread(target=sc.complementary_task, args=(full_path,session.get('user_id'),user_filename),daemon=True)
                deamon.start()
                return render_template('complementary.html', message="Doing the job, check the history")
            else:
                if validate.is_fasta_file_with_only_nucleotide(full_path) != True:
                    message = validate.is_fasta_file_with_only_nucleotide(full_path)
                return render_template('complementary.html', message=message)
        else:
            return render_template('complementary.html',message="All the fields are required")


@dna_controller.route('/split_fasta', methods=['GET', 'POST'])
def split_fasta():
    "Split a fasta file sequence into a desired section"
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('split.html')
    if request.method == 'POST':
        fasta = request.files["split"]
        start = request.form['start']
        end = request.form['end']
        user_filename = request.form['user_filename']
        # print(fasta.filename == "")
        are_file = fasta.filename != "" 
        are_start = start != ""
        are_end = end != ""
        if are_file == True and are_start == True and are_end == True:
            fasta_ext = fasta.filename
            fasta.save(os.path.join(SPLIT_FASTA,fasta_ext))
            full_path = os.path.join(SPLIT_FASTA,fasta_ext)
            if validate.validate_split_fasta(full_path,start,end) == True and user_filename != "":
                daemon = Thread(target=sc.split_fasta_task, args=(full_path,session.get('user_id'),start,end,user_filename),daemon=True)
                daemon.start()
                return render_template('split.html', message="Doing the job, check the history")
            elif validate.validate_split_fasta(full_path,start,end) != True:
                message = validate.validate_split_fasta(full_path,start,end)
                return render_template('split.html',message=message)
            else:
                message = "All the fields are required"
                return render_template('split.html', message=message)
        else:
            if are_file == False or are_start == False or are_end == False:
                message = "All the fields are required"
                return render_template('split.html', message=message)
            # elif validate.validate_split_fasta(full_path) != True:

            # elif:
            #     message = validate.validate_split_fasta(full_path,start,end)
            #     return render_template('split.html', message=message)
            else:
                message = "All the fields are required"
                return render_template('split.html', message=message)


    # return render_template('split.html')

@dna_controller.route('/reverse_complementary',methods=['GET', 'POST'])
def reverse_complementary():
    """Show the cds extract page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET': 
        return render_template('reverse_complementary.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['reverse_complementary']
        user_filename = request.form['user_filename']
        are_file = file.filename != ""
        are_user_filename = user_filename != ""
        if are_file == True and are_user_filename == True:
            # Excecute the cds extract program
            fullroute=sc.save_fasta_file(file,REVERSE)
            if validate.is_fasta_file_with_only_nucleotide(fullroute) == True and user_filename != "" and validate.check_mime_type(fullroute) == "text/plain":
                user_id = session.get('user_id')
                daemon = Thread(target=sc.reverse_complementary_task, args=(fullroute,user_id,user_filename))
                daemon = daemon.start()
                return render_template('reverse_complementary.html',message="Doing the job, check the history")
            else:
                if validate.check_mime_type(fullroute) != "text/plain":
                    return render_template('reverse_complementary.html',message="it needs to be a fasta")
                elif validate.is_fasta_file_with_only_nucleotide(fullroute) != True:
                    message = validate.is_fasta_file_with_only_nucleotide(fullroute)
                    return render_template('reverse_complementary.html',message=message)
                message =validate.is_fasta_file_with_only_nucleotide(fullroute)
                return render_template('reverse_complementary.html',message=message)
        else:
            return render_template('reverse_complementary.html',message="All the fields are required")