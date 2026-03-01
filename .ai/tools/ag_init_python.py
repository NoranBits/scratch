import os
import subprocess
import argparse
import sys
from pathlib import Path

def get_workspace_root():
    """Canonical root discovery."""
    current = os.path.abspath(os.path.dirname(__file__))
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, ".ai")):
            return current
        current = os.path.dirname(current)
    return os.path.abspath(os.getcwd())

def init_python_project(name, target_dir, dry_run=True):
    abs_path = os.path.abspath(os.path.join(target_dir, name))
    print(f"--- Initializing Python Project: {name} ---")
    print(f"Target Path: {abs_path}")
    print(f"Mode: {'DRY RUN' if dry_run else 'ACTIVE'}")

    if dry_run:
        print("[!] dry-run: Would create directory, venv, and basic structure.")
        return

    # Create directory
    os.makedirs(abs_path, exist_ok=True)
    
    # Create .venv
    print(f"Creating virtual environment in {abs_path}...")
    subprocess.run([sys.executable, "-m", "venv", os.path.join(abs_path, ".venv")], check=True)
    
    # Create structure
    os.makedirs(os.path.join(abs_path, "src"), exist_ok=True)
    os.makedirs(os.path.join(abs_path, "tests"), exist_ok=True)
    
    # Create requirements.txt
    with open(os.path.join(abs_path, "requirements.txt"), "w") as f:
        f.write("# Project dependencies\n")
    
    # Create .ai/ markers
    ai_dir = os.path.join(abs_path, ".ai")
    os.makedirs(ai_dir, exist_ok=True)
    with open(os.path.join(ai_dir, "INDEX.md"), "w") as f:
        f.write(f"# {name}\n\nProject initialized via AntiGravity routine.\n")

    print(f"SUCCESS: Python project {name} initialized at {abs_path}")

def main():
    parser = argparse.ArgumentParser(description="AG Python Project Initializer")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--path", default=".", help="Target parent directory")
    parser.add_argument("--write", action="store_true", help="Authorize active initialization")

    args = parser.parse_args()
    init_python_project(args.name, args.path, dry_run=not args.write)

if __name__ == "__main__":
    main()
