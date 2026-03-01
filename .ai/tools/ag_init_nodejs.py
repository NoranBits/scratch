import os
import subprocess
import argparse
import json
import sys

def init_nodejs_project(name, target_dir, dry_run=True):
    abs_path = os.path.abspath(os.path.join(target_dir, name))
    print(f"--- Initializing Node.js Project: {name} ---")
    print(f"Target Path: {abs_path}")
    print(f"Mode: {'DRY RUN' if dry_run else 'ACTIVE'}")

    if dry_run:
        print("[!] dry-run: Would create directory, run npm init, and set up structure.")
        return

    # Create directory
    os.makedirs(abs_path, exist_ok=True)
    
    # npm init -y
    print(f"Running npm init -y in {abs_path}...")
    subprocess.run(["npm", "init", "-y"], cwd=abs_path, shell=True, check=True)
    
    # Update package.json
    pkg_path = os.path.join(abs_path, "package.json")
    with open(pkg_path, "r") as f:
        pkg = json.load(f)
    
    pkg["scripts"]["ag-audit"] = "python ../.ai/tools/ag_security_scanner.py --path ."
    pkg["scripts"]["ag-sync"] = "python ../.ai/tools/ag_intent_sync.py"
    
    with open(pkg_path, "w") as f:
        json.dump(pkg, f, indent=2)
    
    # Create structure
    os.makedirs(os.path.join(abs_path, "src"), exist_ok=True)
    
    # Create .ai/ markers
    ai_dir = os.path.join(abs_path, ".ai")
    os.makedirs(ai_dir, exist_ok=True)
    with open(os.path.join(ai_dir, "INDEX.md"), "w") as f:
        f.write(f"# {name}\n\nProject initialized via AntiGravity routine.\n")

    print(f"SUCCESS: Node.js project {name} initialized at {abs_path}")

def main():
    parser = argparse.ArgumentParser(description="AG Node.js Project Initializer")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--path", default=".", help="Target parent directory")
    parser.add_argument("--write", action="store_true", help="Authorize active initialization")

    args = parser.parse_args()
    init_nodejs_project(args.name, args.path, dry_run=not args.write)

if __name__ == "__main__":
    main()
