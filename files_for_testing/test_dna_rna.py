import subprocess
import os

path = os.getcwd()
print(path)


def test_dna_rna(file):
    subprocess.run([path+"/dna_rna", file])

test_dna_rna(path+"files_for_testing/test_dna_protein/sequence.fasta")