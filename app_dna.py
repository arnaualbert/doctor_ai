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


@dna_controller.route('/dnatoprotein',methods=['GET', 'POST'])
def DNA_to_protein():
    """Show the dna to protein page"""
    if not logins.is_logged(): return render_template('login.html')
    
    if request.method == 'GET': 
        return render_template('dna_protein.html')
    
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnaprotein']
        if file:
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            fullroute = sc.save_fasta_file_with_id(id,file,DNATOPROTEIN)
            # Excecute the dna to protein program
            if validate.is_fasta_file_with_only_ATGC(fullroute):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_protein, args=(fullroute,filename,user_id,id))
                daemon = daemon.start()
            return render_template('dna_protein.html')  


    
@dna_controller.route('/dnatorna',methods=['GET', 'POST'])
def DNA_to_RNA():
    """Show the dna to rna page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET': 
        return render_template('dna_rna.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['dnarna']
        if file:
            id = randint(1,9999999)
            ids = str(id)
            filename = ids+file.filename
            fullroute = sc.save_fasta_file_with_id(id,file,DNATORNA)
            if validate.is_fasta_file_with_only_ATGC(fullroute):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.dna_to_rna, args=(fullroute,filename,user_id,id))
                daemon = daemon.start()
                return render_template('dna_rna.html')
            else:
                return render_template('dna_rna.html')
            

@dna_controller.route("/complementary", methods=['GET', 'POST'])
def complementary():
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('complementary.html')
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
        fasta_ext = fasta.filename
        fasta.save(os.path.join(SPLIT_FASTA,fasta_ext))
        full_path = os.path.join(SPLIT_FASTA,fasta_ext)
        if validate.validate_split_fasta(full_path,start,end):
            daemon = Thread(target=sc.split_fasta_task, args=(full_path,session.get('user_id'),start,end),daemon=True)
            daemon.start()
            return render_template('split.html', message="Doing the job")
        else:
            # os.remove(full_path)
            return render_template('split.html', message="File must be in .fasta format and inputs must be numbers bigger tha 0")

    return render_template('split.html')

@dna_controller.route('/reverse_complementary',methods=['GET', 'POST'])
def reverse_complementary():
    """Show the cds extract page"""
    if not logins.is_logged(): return render_template('login.html')

    if request.method == 'GET': 
        return render_template('reverse_complementary.html')
    if request.method == 'POST':
        # Get the data from the form
        file = request.files['reverse_complementary']
        if file:
            # Excecute the cds extract program
            fullroute=sc.save_fasta_file(file,REVERSE)
            if validate.is_fasta_file_with_only_ATGC(fullroute):
                user_id = session.get('user_id')
                daemon = Thread(target=sc.reverse_complementary_task, args=(fullroute,user_id))
                daemon = daemon.start()
                return render_template('reverse_complementary.html')
        return render_template('reverse_complementary.html')