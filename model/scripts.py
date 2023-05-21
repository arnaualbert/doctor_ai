import  os 
import subprocess
import os
import model.upload as upload
from pathlib import Path
import re
########
from multiprocessing import Pool
from random import *
import subprocess
import model.user as user
import model.roles as role
path = os.getcwd()

def generate_unique_id() -> str:
    """Generate unique identifier for result in database"""
    while True:
        id = str(randint(1, 9999999))
        result = upload.select_from_where_id("id", "results", id)
        if result is None:
            return id


def tuple_to_object(result):
    """ Convert tuple to object 
    input:
        result: tuple
    output:
        object type (user.User)
    """
    id = result[0]
    username = result[1]
    name = result[2]
    surname = result[3]
    email = result[4]
    password = result[5]
    role_id = result[6]

    return user.User(username,name,surname,email, password, role_id,id)

def dict_to_role(result):
    """ Convert tuple to object 
    input:
        result: tuple
    output:
        object type (user.User)
    """
    id = result["id"]
    role_name = result["role_name"]
    return role.Roles(id,role_name)

def save_fasta_file(fasta, directory) -> Path:
    """
    This function saves a fasta file to a directory and returns the filepath
    Input:
        fasta: fasta file
        directory: directory to save the file
    Output:
        saved file path
    """
    id = randint(1, 9999999)
    filename = fasta.filename
    ids = str(id)
    filename = ids + filename
    filepath = os.path.join(directory, filename)
    fasta.save(filepath)
    return filepath


def save_fasta_file_with_id(id,file, directory):
    """
    This function saves a fasta file to a directory and returns the filepath
    Input:
        fasta: fasta file
        directory: directory to save the file
    Output:
        saved file path
    """
    ids = str(id)
    filename = ids+file.filename
    file.save(os.path.join(directory, filename))
    fullroute=os.path.join(directory, filename)
    return fullroute

def random_sequence_task(number,user_id,user_filename):
    """Execute the random sequence program and return the new filename
    Input:
        number: number of random sequences
        user_id: user id
    Output:
        Upload results to the database
    """
    id = randint(1, 9999999)
    ids = str(id)
    new_id: str = generate_unique_id()
    file_up = "dna.fasta"
    query = "random_sequence"
    final_filename = user_filename + '.fasta'
    print("number")
    print(number)
    print("user_id")
    print(user_id)
    a = upload.upload_results(id,query,user_id,final_filename)   
    subprocess.run(["./random", number])
    new_filename = re.sub(r'\.fasta$', new_id+'random.fasta', file_up)
    os.rename(file_up, new_filename)
    # b = upload.update_date(id,new_filename,user_id)
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(new_filename)


def complementary_task(fasta,user_id,user_filename):
    """Execute the complementary program 
    Input:
        fasta: fasta file
        user_id: user id
    Output:
        Upload results to the database
    """
    id = randint(1, 9999999)
    # out_name = f"{id}complementary.fasta"
    out_name = user_filename + '.fasta'
    query = "complementary"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)
    subprocess.run(["./complementary",fasta,out_name])
    file_to_read = open(out_name).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(out_name)
    os.remove(fasta)

def reverse_complementary_task(fasta,user_id,user_filename):
    """Execute the reverse complementary program
    Input:
        fasta: fasta file
        user_id: user id
    Output:
        Upload results to the database
    """
    id = randint(1, 9999999)
    out_name = f"{id}reverse_complementary.fasta"
    query = "reverse_complementary"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)
    subprocess.run(["./reverse_complementary",fasta,out_name])
    file_to_read = open(out_name).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(out_name)
    os.remove(fasta)

def split_fasta_task(fasta, user_id,start,end,user_filename):
    """Execute the split fasta program
    Input:
        fasta: fasta file
        user_id: user id
        start: start position
        end: end position
    Output:
        Upload results to the database
    """
    query = "split_fasta"
    id = randint(1, 9999999)
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)
    subprocess.run(["./split",fasta,start,end])
    # subprocess.run(f"./split {fasta} {start} {end} &")
    file_up = f"output_{start}_{end}.fasta"
    new_filename = re.sub(r'\.fasta$', str(id)+'output_'+start+'_'+end+'.fasta', file_up)
    os.rename(file_up, new_filename)
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(fasta)
    os.remove(new_filename)


def genbank_to_fasta(fullroute,user_id,user_filename):
    """Execute the genbank to fasta program
    Input:
        fullroute: fullroute to the fasta file
        user_id: user id
    Output: 
        Upload results to the database
    """
    id = randint(1,9999999)
    ids = str(id)
    file_up = Path('gb_to_fasta.fasta')
    query = "gb_to_fasta"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)  
    subprocess.run(["./genbankToFastaV3",fullroute])
    new_filename = Path(ids+'gb_to_fasta.fasta')
    asd = file_up.rename(new_filename)
    file_to_read = open(asd).read()
    upload.update_date(id,file_to_read,user_id)


def cdsextract_task(fullroute,user_id,user_filename):
    """Execute the cdsextract program
    Input:
        fullroute: fullroute to the fasta file
        user_id: user id
    Output:
        Upload results to the database
    """
    id = randint(1,9999999)
    ids = str(id)
    file_up = Path('resultado.fasta')
    query = "cds_extract"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)  
    subprocess.run(["./extract_cds",fullroute])
    new_filename = Path(ids+'resultado.txt')
    asd = file_up.rename(new_filename)
    file_to_read = open(asd).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(fullroute)
    os.remove(asd)


def dna_to_rna(fullroute,filename,user_id,id,user_filename):
    """Execute the dna to rna program
    Input:
        fullroute: fullroute to the fasta file
        user_id: user id
        id: id
        filename: filename
    Output:
        Upload results to the database"""
    query = "dna_to_rna"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)
    subprocess.run(["./dna_rna",fullroute,user_filename])
    file_up = "./"+user_filename
    file_to_read = open(file_up).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(user_filename)
    os.remove(fullroute)

def dna_to_protein(fullroute,filename,user_id,id,user_filename):
    """Execute the dna to protein program
    Input:
        fullroute: fullroute to the fasta file
        user_id: user id
        id: id
        filename: filename
    Output:
        Upload results to the database
    """
    query = "dnaprotein"
    final_filename = user_filename + '.fasta'
    upload.upload_results(id,query,user_id,final_filename)
    subprocess.run(["./dna_protein",fullroute,user_filename])
    file_up = "./"+user_filename
    file_to_read = open(file_up).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(user_filename)
    os.remove(fullroute)

def local(fasta1_filepath, fasta2_filepath, match, mismatch, gap,gapLeft, gapUp,user_id,user_filename):
    """Execute the local alignment program
    Input:
        fasta1_filepath: fasta file
        fasta2_filepath: fasta file
        user_id: user id
        match: match score
        mismatch: mismatch score
        gap: gap score
        gapLeft: gapLeft score
        gapUp: gapUp score
    Output:
        Upload results to the database
    """
    id = randint(1,9999999)
    ids = str(id)
    file_up = "alignment_result.txt"
    query = "local_alignment"
    final_filename = user_filename + '.txt'
    upload.upload_results(id,query,user_id,final_filename)
    print("running local alignment")
    subprocess.run(["./local_alignment",fasta1_filepath, fasta2_filepath, match, mismatch, gap,gapLeft, gapUp, user_filename])
    print("finished local alignment")
    new_filename = "./"+user_filename
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(new_filename)
    os.remove(fasta1_filepath)
    os.remove(fasta2_filepath)



def blosum_local(fasta1_filepath, fasta2_filepath, gap,gap_extend,user_id,user_filename):
    """Execute the local alignment program with blosum
    Input:
        fasta1_filepath: fasta file
        fasta2_filepath: fasta file
        user_id: user id
        user_filename: user filename
        gap: gap score
        gap_extend: gap extend
    Output:
        Upload results to the database
    """
    id = randint(1,9999999)
    query = "blosum_local_alignment"
    final_filename = user_filename + '.txt'
    upload.upload_results(id,query,user_id,final_filename)
    print("running local alignment")
    subprocess.run(["./blosum",fasta1_filepath, fasta2_filepath,gap,gap_extend,user_filename])
    print("finished Blosum local alignment")
    new_filename = "./"+user_filename
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(new_filename)
    os.remove(fasta1_filepath)
    os.remove(fasta2_filepath)

def blosum_global(fasta1_filepath, fasta2_filepath, gap,gap_extend,user_id,user_filename):
    id = randint(1,9999999)
    ids = str(id)
    file_up = "global_alignment_result.txt"
    query = "blosum_global_alignment"
    final_filename = user_filename + '.txt'
    upload.upload_results(id,query,user_id,final_filename)
    print("running global alignment")
    subprocess.run(["./global_alignment_blosum",fasta1_filepath, fasta2_filepath,gap,gap_extend])
    print("finished Blosum global alignment")
    new_filename = re.sub(r'\.txt$',ids+'alignment_result_blosum.txt', file_up)
    print(new_filename)
    os.rename(file_up, new_filename)
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(new_filename)
    os.remove(fasta1_filepath)
    os.remove(fasta2_filepath)


def run_global_align(fasta1_filepath, fasta2_filepath, match, mismatch, gap,user_id,user_filename):
    """Execute the local alignment program
    Input:
        fasta1_filepath: fasta file
        fasta2_filepath: fasta file
        user_id: user id
        match: match score
        mismatch: mismatch score
        gap: gap score
        gapLeft: gapLeft score
        gapUp: gapUp score
    Output:
        Upload results to the database
    """
    id = generate_unique_id()
    file_up = "alignment_result.txt"
    query = "global_alignment"
    final_filename = user_filename + '.txt'
    upload.upload_results(id,query,user_id,final_filename)
    print("running global alignment")
    subprocess.run(["./global_alignment",fasta1_filepath, fasta2_filepath, match, mismatch, gap, user_filename])
    print("finished global alignment")
    new_filename = "./"+user_filename
    file_to_read = open(new_filename).read()
    upload.update_date(id,file_to_read,user_id)
    os.remove(new_filename)
    os.remove(fasta1_filepath)
    os.remove(fasta2_filepath)
