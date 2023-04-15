import  os 
import subprocess

path = os.getcwd()

def dna_rna(file):
    subprocess.run([path+"/dna_rna", file])

def dna_protein(file):
    subprocess.run([path+"/dna_protein", file])

def extract_cds(file):
    subprocess.run([path+"/extract_cds", file])

def random_seq(length):
    subprocess.run([path+"/random", length])

def local_alignment(file1,file2):
    subprocess.run([path+"/local_alignment", file1, file2])

def global_alignment(file1,file2):
    subprocess.run([path+"/global_aligment", file1, file2])

def gb_to_fasta(file):
    subprocess.run([path+"/genbankToFastaV3", file])