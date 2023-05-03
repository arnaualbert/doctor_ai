import  os 
import subprocess
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
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
executor = ThreadPoolExecutor(5)
########
from multiprocessing import Pool
from random import *
import subprocess
import multiprocessing

path = os.getcwd()

def save_fasta_file(fasta, directory):
    filename = fasta.filename
    filepath = os.path.join(directory, filename)
    fasta.save(filepath)
    return filepath



def dna_rna(file):
    subprocess.run([path+"/dna_rna", file])

def dna_protein(file):
    subprocess.run([path+"/dna_protein", file])

def extract_cds(file):
    subprocess.run([path+"/extract_cds", file])

# def random_seq(length):
def random_sequence_task(number,user_id):
    """Execute the random sequence program and return the new filename"""
    id = randint(1, 9999999)
    ids = str(id)
    file_up = "dna.fasta"
    query = "random_sequence"
    a = upload.upload_results(id,query,user_id)   
    subprocess.run(["./random", number])
    new_filename = re.sub(r'\.fasta$', ids+'random.fasta', file_up)
    os.rename(file_up, new_filename)
    b = upload.update_date(id,new_filename,user_id)              
    print(a)     
    print(b)
    print(new_filename)
    return new_filename
    # subprocess.run([path+"/random", length])

def local_alignment(file1,file2):
    subprocess.run([path+"/local_alignment", file1, file2])

def global_alignment(file1,file2):
    subprocess.run([path+"/global_aligment", file1, file2])

def gb_to_fasta(file):
    subprocess.run([path+"/genbankToFastaV3", file])


def complementary_task(fasta,user_id):
    id = randint(1, 9999999)
    out_name = f"{id}complementary.fasta"
    query = "complementary"
    upload.upload_results(id,query,user_id)
    subprocess.run(["./complementary",fasta,out_name])
    upload.update_date(id,out_name,user_id)


def split_fasta_task(fasta, user_id,start,end):
    query = "split_fasta"
    id = randint(1, 9999999)
    upload.upload_results(id,query,user_id)
    subprocess.run(["./split",fasta,start,end])
    file_up = f"output_{start}_{end}.fasta"
    new_filename = re.sub(r'\.fasta$', str(id)+'output_'+start+'_'+end+'.fasta', file_up)
    os.rename(file_up, new_filename)
    upload.update_date(id,new_filename,user_id)


def genbank_to_fasta(fullroute,user_id):
    id = randint(1,9999999)
    ids = str(id)
    file_up = Path('gb_to_fasta.fasta')
    query = "gb_to_fasta"
    upload.upload_results(id,query,user_id)  
    subprocess.run(["./genbankToFastaV3",fullroute])
    new_filename = Path(ids+'gb_to_fasta.fasta')
    asd = file_up.rename(new_filename)
    upload.update_date(id,asd,user_id)


def cdsextract_task(fullroute,user_id):
    id = randint(1,9999999)
    ids = str(id)
    file_up = Path('resultado.fasta')
    query = "cds_extract"
    upload.upload_results(id,query,user_id)  
    subprocess.run(["./extract_cds",fullroute])
    new_filename = Path(ids+'resultado.txt')
    asd = file_up.rename(new_filename)
    upload.update_date(id,asd,user_id)


def dna_to_rna(fullroute,filename,user_id,id):
    query = "dna_to_rna"
    upload.upload_results(id,query,user_id)
    subprocess.run(["./dna_rna",fullroute])
    new_filename = re.sub(r'\.fasta$', '_modified.fasta', filename)
    file_up = "dnatorna/"+new_filename
    upload.update_date(id,file_up,user_id)

def dna_to_protein(fullroute,filename,user_id,id):
    query = "dnaprotein"
    upload.upload_results(id,query,user_id)
    subprocess.run(["./dna_protein",fullroute])
    new_filename = re.sub(r'\.fasta$', '_protein.fasta', filename)
    file_up = "dnaprotein/"+new_filename
    upload.update_date(id,file_up,user_id)


def local(fasta1_filepath, fasta2_filepath, match, mismatch, gap,user_id):
        # Execute the local aligment program
    id = randint(1,9999999)
    ids = str(id)
    file_up = "alignment_result.txt"
    query = "local_alignment"
    upload.upload_results(id,query,user_id)
    print("running local alignment")
    subprocess.run(["./local_alignment",fasta1_filepath, fasta2_filepath, match, mismatch, gap])
    print("finished local alignment")
    new_filename = re.sub(r'\.txt$',ids+'alignment_result.txt', file_up)
    print(new_filename)
    os.rename(file_up, new_filename)
    upload.update_date(id,new_filename,user_id)