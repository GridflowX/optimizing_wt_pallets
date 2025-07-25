import subprocess
import os

def run(script_path):
    print(f"\nRunning {script_path}...\n")
    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )

    if result.stdout:
        print("STDOUT:")
        print(result.stdout)

    if result.stderr:
        print("STDERR:")
        print(result.stderr)

    if result.returncode != 0:
        print(f"Script failed: {script_path}")
        exit(result.returncode)
    else:
        print(f"Completed: {script_path}\n")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths to each experiment script
scripts = [
    os.path.join(current_dir, "exp1", "run_all_exp1.py"),
    os.path.join(current_dir, "exp2", "run_all_exp2.py"),
    os.path.join(current_dir, "exp3", "run_all_exp3.py"),
    os.path.join(current_dir, "exp4", "run_all_exp4.py"),
]

for script in scripts:
    run(script)

print("All experiments completed.")
