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


def is_fasta_file_with_only_nucleotide(filename: str) -> bool and str:
    """Check if a file is a fasta file with only ATGC
    input: str
    output: bool and str
    if the file is a fasta file with only ATGC return True
    else return a message"""
    if check_mime_type(filename) == "text/plain":
        print(check_mime_type(filename))
        if filename.endswith('.fasta'):
            with open(filename) as f:
                first_line = f.readline().strip()
                if not first_line.startswith('>') or first_line.startswith(';'):
                    return "It needs to start with > to be a fasta file"
                for line in f:
                    if line.startswith('>'):
                        continue
                    if any(letter not in 'ATGC' for letter in line.strip()):
                        return "It needs to be a nucleotide"
                else:
                    return True
        else:
            return "It needs to be a fasta file"
    else:
        print(check_mime_type(filename))
        return "It's not a fasta file"

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

def validate_split_fasta(full_path,start:str,end:str) -> bool and str:
    """validate if the inputs are correct"""
    if full_path != None and start != None and end != None and is_fasta_file_with_only_nucleotide(full_path) == True and int(start)>0 and int(end)>0 and start.isnumeric() and end.isnumeric() and int(start)<=count_letters_in_file(full_path) and int(end)<=count_letters_in_file(full_path) and check_mime_type(full_path) == "text/plain":
        return True
    else:
        if check_mime_type(full_path) != "text/plain":
            return "File must be in .fasta format"
        elif int(start)<0:
            return "Start must be greater than 0"
        elif int(end)<0:
            return "End must be greater than 0"
        elif int(start)>count_letters_in_file(full_path):
            return f"Start must be less than the number of letters in the file it have {count_letters_in_file(full_path)} letters"
        elif int(end)>count_letters_in_file(full_path):
            return f"End must be less than the number of letters in the file it have {count_letters_in_file(full_path)} letters"
        elif start.isnumeric() == False:
            return "Start must be a number"
        elif end.isnumeric() == False:
            return "End must be a number"
        elif int(start)>int(end):
            return "Start must be less than End"
        elif is_fasta_file_with_only_nucleotide(full_path) != True:
            return is_fasta_file_with_only_nucleotide(full_path)


def validate_local_aligment(fasta1: str,fasta2: str,match: int,mismatch: int,gap: int,gapLeft: int,gapUp: int) -> bool:
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_nucleotide(fasta1) and is_fasta_file_with_only_nucleotide(fasta2) and match != None and mismatch != None and gap != None and gapLeft != None and gapUp != None and int(gapLeft) < 0 and int(gapUp) < 0 and check_mime_type(fasta1) == "text/plain":
        return True
    else:
        if check_mime_type(fasta1) != "text/plain":
            return "File must be in .fasta format"
        elif check_mime_type(fasta2) != "text/plain":
            return "File must be in .fasta format"
        elif int(gapUp) > 0:
            return "The gap extend Up must be negative"
        elif int(gapLeft) > 0:
            return "The gap extend Left must be negative"
        elif gapUp == None :
            return "You must fill the gap extend Up input"
        elif gapLeft == None :
            return "You must fill the gap extend Left input"
        elif gap == None :
            return "You must fill the gap input"
        elif mismatch == None :
            return "You must fill the mismatch input"
        elif match == None :
            return "You must fill the match input"
        elif is_fasta_file_with_only_nucleotide(fasta1) != True:
            return is_fasta_file_with_only_nucleotide(fasta1)
        elif is_fasta_file_with_only_nucleotide(fasta2) != True:
            return is_fasta_file_with_only_nucleotide(fasta2)
    
def validate_blosum_local_aligment(fasta1: str,fasta2: str,gap: int,gap_extend: int) -> bool:
    """validate if the inputs are correct"""
    if fasta1 !=None and fasta2 != None and gap != None and gap_extend != None:
        return True
    else:
        if check_mime_type(fasta2) != "text/plain":
            return "File must be in .fasta format"
        elif check_mime_type(fasta1) != "text/plain":
            return "File must be in .fasta format"
        elif gap_extend == None :
            return "You must fill the gap extend input"
        elif gap == None :
            return "You must fill the gap input"
        elif fasta2 == None:
            return "You must fill Target fasta input"
        elif fasta1 == None:
            return "You must fill Query fasta input"

def validate_GA_form(fasta1: str,fasta2: str,match: int,mismatch: int,gap: int) -> bool:
    """validate if the inputs are correct"""
    if is_fasta_file_with_only_nucleotide(fasta1) and is_fasta_file_with_only_nucleotide(fasta2) and match != None and mismatch != None and gap != None:
        return True
    else:
        if check_mime_type(fasta2) != "text/plain":
            return "File must be in .fasta format"
        elif check_mime_type(fasta1) != "text/plain":
            return "File must be in .fasta format"
        elif gap == None :
            return "You must fill the gap input"
        elif mismatch == None :
            return "You must fill the mismatch input"
        elif match == None :
            return "You must fill the match input"
        elif is_fasta_file_with_only_nucleotide(fasta1) != True:
            return is_fasta_file_with_only_nucleotide(fasta1)
        elif is_fasta_file_with_only_nucleotide(fasta2) != True:
            return is_fasta_file_with_only_nucleotide(fasta2)
    

def is_genbank(gb_filepath: str) -> bool | str:
    """Validate if a input file is a genbank file"""   
    if gb_filepath.endswith(".gb"):
        print(os.stat(gb_filepath).st_size)
        if os.stat(gb_filepath).st_size > 0:
            with open(gb_filepath, 'r') as file:
                first_line = file.readline().strip()
                if first_line.startswith("LOCUS") and "bp" in first_line:
                    return True
                else:
                    return "File must be in .gb format"
        else:
            print(os.stat(gb_filepath).st_size)
            return "File is empty"
    else:
        return "File must be in .gb format"

