import subprocess
import os
import sys
from pathlib import Path

def find_git_bash():
    paths = [
        r"C:\Program Files\Git\bin\bash.exe",
        r"C:\Program Files\Git\usr\bin\bash.exe",
        r"C:\Program Files (x86)\Git\bin\bash.exe",
        os.path.expanduser("~") + r"\AppData\Local\Programs\Git\bin\bash.exe"
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return "bash" # Fallback to PATH

def main():
    bash_path = find_git_bash()
    ROOT = Path(__file__).parent.parent.parent
    
    # If no arguments, just launch an interactive shell
    if len(sys.argv) == 1:
        print(f"Launching AntiGravity Git Bash at {ROOT}...")
        subprocess.run([bash_path, "--login", "-i"], cwd=ROOT)
    else:
        # Run passed command
        cmd = sys.argv[1:]
        subprocess.run([bash_path, "-c", " ".join(cmd)], cwd=ROOT)

if __name__ == "__main__":
    main()
