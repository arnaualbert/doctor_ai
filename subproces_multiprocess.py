from multiprocessing import Pool
import subprocess
import multiprocessing


def z(x):
    return subprocess.run(["./1_team_members/luis/luis",x])
def i(x):
    return subprocess.run(["./1_team_members/arnau/hello"])

if __name__ == '__main__':
    cpu = multiprocessing.cpu_count() - 1
    with Pool(5)as p:
        results = p.map(z, ["atgctagctagctgact", "atcgatcga","gtcagtcgatgctgactgatgcta"])
        results = p.map(i, ["atgctagctagctgact", "atcgatcga"])