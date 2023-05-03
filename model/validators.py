import os
from PIL import Image 

def is_image_file(filepath):
    """Check if a file is an image trying to open it as an image""" 
    try:
        with Image.open(filepath) as image:
            return True
    except:
        return False

def is_fasta_file_with_only_ATGC(filename):
    """Check if a file is a fasta file with only ATGC"""
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
    """Read a fasta file"""
    file_extension = os.path.splitext(file_path)[1]
    if file_extension not in ['.fasta', '.fa']:
        # raise ValueError("File must be in .fasta or .fa format")
        return False
    else:
        return True


def count_letters_in_file(filename):
    """Count the number of letters in a file"""
    with open(filename, "r") as file:
        next(file)
        count = 0
        for line in file:
            count += len(line.strip())

    return count

def validate_split_fasta(full_path,start:str,end:str):
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_ATGC(full_path) and int(start)>0 and int(end)>0 and start.isnumeric() and end.isnumeric() and int(start)<=count_letters_in_file(full_path) and int(end)<=count_letters_in_file(full_path):
        return True
    else:
        return False


def validate_local_aligment(fasta1,fasta2,match,mismatch,gap):
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_ATGC(fasta1) and is_fasta_file_with_only_ATGC(fasta2) and match != None and mismatch != None and gap != None:
        return True
    else:
        return False
