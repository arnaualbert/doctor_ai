import multiprocessing
import subprocess

def run_go_script(go_script_path):
    """ Function to run a Go script using subprocess """
    print(f"Running script {go_script_path}")
    subprocess.call(['go', 'run', go_script_path])

if __name__ == '__main__':
    # List of Go script paths to be executed
    go_script_paths = ['1_team_members/luis/script1.go', '1_team_members/luis/script2.go', '1_team_members/luis/script3.go']

    # Create a process pool of 3 workers
    with multiprocessing.Pool(processes=3) as pool:
        # Map the run_go_script function to the go_script_paths list
        pool.map(run_go_script, go_script_paths)
