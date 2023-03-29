from multiprocessing import Pool
import subprocess

def f(x):
    return subprocess.check_output(["./1_team_members/arnau/hello", str(x)])

if __name__ == '__main__':
    with Pool(5) as p:
        results = p.map(f, [1, 2, 3, 4, 5])
    for result in results:
        print(result)

