import subprocess
import json
import os
from pathlib import Path

PHASES = [
    "dev",
    "demos",
    "alphas",
    "betas",
    "open-betas",
    "production",
    "maintenance"
]

def get_git_info(cwd):
    info = {
        "is_repo": False,
        "branch": "N/A",
        "last_commit": "None",
        "remotes": [],
        "status": "No Repo",
        "phases": {}
    }
    
    try:
        # Check if it's a repo
        subprocess.check_output(["git", "rev-parse", "--is-inside-work-tree"], cwd=cwd, stderr=subprocess.STDOUT)
        info["is_repo"] = True
        
        # Current Branch
        info["branch"] = subprocess.check_output(["git", "branch", "--show-current"], cwd=cwd).decode().strip()
        
        # Last commit
        info["last_commit"] = subprocess.check_output(["git", "log", "-1", "--format=%h - %s (%cr)"], cwd=cwd).decode().strip()
        
        # Remotes
        remotes_raw = subprocess.check_output(["git", "remote", "-v"], cwd=cwd).decode().strip()
        if remotes_raw:
            info["remotes"] = list(set([line.split()[0] for line in remotes_raw.splitlines()]))
            
        # Status (short)
        status_raw = subprocess.check_output(["git", "status", "--short"], cwd=cwd).decode().strip()
        info["status"] = "Clean" if not status_raw else f"{len(status_raw.splitlines())} changes"
        
        # Phase Audit
        for phase in PHASES:
            try:
                # Get last commit for each phase branch
                last_c = subprocess.check_output(["git", "log", "-1", "--format=%h (%cr)", phase], cwd=cwd, stderr=subprocess.DEVNULL).decode().strip()
                info["phases"][phase] = {
                    "last_commit": last_c,
                    "exists": True
                }
            except subprocess.CalledProcessError:
                info["phases"][phase] = {"exists": False}
                
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
        
    return info

if __name__ == "__main__":
    ROOT = Path(__file__).parent.parent.parent
    git_data = get_git_info(ROOT)
    
    output_path = ROOT / ".ai" / "git_status.json"
    with open(output_path, "w") as f:
        json.dump(git_data, f, indent=2)
    
    print(f"Git Pulse generated at {output_path}")
