import subprocess
import json
import os
from datetime import datetime

PHASES = ["dev", "demos", "alphas", "betas", "open-betas", "production", "maintenance"]

def get_git_info():
    try:
        # Check if it's a git repo
        is_repo = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True).stdout.strip() == "true"
        if not is_repo:
            return {"is_repo": false}

        # Current branch
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
        
        # Last commit
        last_commit = subprocess.run(["git", "log", "-1", "--format=%h - %s (%cr)"], capture_output=True, text=True).stdout.strip()
        
        # Remotes
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout.strip().split("\n")
        
        # Status
        status_raw = subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout.strip()
        status = f"{len(status_raw.splitlines())} changes" if status_raw else "Clean"
        
        # Phase Scanning
        phases = {}
        for p in PHASES:
            exists = subprocess.run(["git", "rev-parse", "--verify", p], capture_output=True).returncode == 0
            if exists:
                last_p = subprocess.run(["git", "log", "-1", p, "--format=%h (%cr)"], capture_output=True, text=True).stdout.strip()
                phases[p] = {"last_commit": last_p, "exists": True}
            else:
                phases[p] = {"exists": False}

        return {
            "is_repo": True,
            "branch": branch,
            "last_commit": last_commit,
            "remotes": [r for r in remotes if r],
            "status": status,
            "phases": phases
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    info = get_git_info()
    output_path = os.path.join(".ai", "git_status.json")
    with open(output_path, "w") as f:
        json.dump(info, f, indent=2)
    print(f"Git Pulse generated at {os.path.abspath(output_path)}")
