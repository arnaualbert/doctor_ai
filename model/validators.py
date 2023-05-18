import os
from PIL import Image 
import magic


def check_mime_type(filepath: str) -> str:
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(filepath)
    return mime_type

def is_image_file(filepath: str) -> bool:
    """Check if a file is an image trying to open it as an image""" 
    try:
        with Image.open(filepath) as image:
            return True
    except:
        return False


def is_fasta_file_with_only_ATGC(filename: str) -> bool:
    """Check if a file is a fasta file with only ATGC"""
    if filename.endswith('.fasta'):
        with open(filename) as f:
            first_line = f.readline().strip()
            if not first_line.startswith('>') or first_line.startswith(';'):
                return False
            for line in f:
                if line.startswith('>'):
                    continue
                if any(letter not in 'ATGC' for letter in line.strip()):
                    return False
        return True
    else:
        return False


def read_fasta_file(file_path: str) -> bool:
    """Read a fasta file"""
    file_extension = os.path.splitext(file_path)[1]
    if file_extension not in ['.fasta', '.fa']:
        # raise ValueError("File must be in .fasta or .fa format")
        return False
    else:
        return True


def count_letters_in_file(filename: str) -> int:
    """Count the number of letters in a file"""
    with open(filename, "r") as file:
        next(file)
        count = 0
        for line in file:
            count += len(line.strip())

    return count

def validate_split_fasta(full_path,start:str,end:str) -> bool:
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_ATGC(full_path) and int(start)>0 and int(end)>0 and start.isnumeric() and end.isnumeric() and int(start)<=count_letters_in_file(full_path) and int(end)<=count_letters_in_file(full_path) and check_mime_type(full_path) == "text/plain":
        return True
    else:
        return False


def validate_local_aligment(fasta1: str,fasta2: str,match: int,mismatch: int,gap: int,gapLeft: int,gapUp: int) -> bool:
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_ATGC(fasta1) and is_fasta_file_with_only_ATGC(fasta2) and match != None and mismatch != None and gap != None and gapLeft != None and gapUp != None and int(gapLeft) < 0 and int(gapUp) < 0:
        return True
    else:
        return False
    
def validate_blosum_local_aligment(fasta1: str,fasta2: str,gap: int,gap_extend: int) -> bool:
    """validate if the inputs are correct"""
    if fasta1 !=None and fasta2 != None and gap != None and gap_extend != None:
        return True
    else:
        return False

def validate_global_aligment(fasta1: str,fasta2: str,match: int,mismatch: int,gap: int) -> bool:
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_ATGC(fasta1) and is_fasta_file_with_only_ATGC(fasta2) and match != None and mismatch != None and gap != None:
        return True
    else:
        return False
    

def is_genbank(gb_filepath: str) -> bool:
    """Validate if a input file is a genbank file"""   
    if gb_filepath.endswith(".gb"):
        with open(gb_filepath, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith("LOCUS") and "bp" in first_line:
                return True
            else:
                return False
    else:
        return False

