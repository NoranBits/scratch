import json
import os
import sys
import urllib.request
from pathlib import Path

def create_github_repo(token, name, private=True):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "private": private,
        "description": "AntiGravity Agentic Workspace - Formed by AG-ORCH protocol."
    }
    
    # Request
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Error creating repo: {e.code} - {e.reason}")
        print(e.read().decode())
        return None

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN environment variable not found.")
        print("Please generate a Personal Access Token (PAT) with 'repo' scope and set it:")
        print("  Windows (PowerShell): $env:GITHUB_TOKEN='your_token'")
        print("  Linux/Mac: export GITHUB_TOKEN='your_token'")
        sys.exit(1)
        
    ROOT = Path(__file__).parent.parent.parent
    REPO_NAME = ROOT.name or "antigravity-workspace"
    
    print(f"Attempting to create GitHub repository: {REPO_NAME}...")
    repo_info = create_github_repo(token, REPO_NAME)
    
    if repo_info:
        remote_url = repo_info["clone_url"]
        # Inject token into URL for authenticated pushes
        auth_url = remote_url.replace("https://", f"https://{token}@")
        
        print(f"Success! Remote URL: {remote_url}")
        
        # Add remote
        try:
            import subprocess
            subprocess.run(["git", "remote", "add", "origin", auth_url], cwd=ROOT, check=True)
            print("Configured remote 'origin'.")
            
            # Initial push
            subprocess.run(["git", "branch", "-M", "master"], cwd=ROOT, check=True)
            subprocess.run(["git", "push", "-u", "origin", "master"], cwd=ROOT, check=True)
            print("Initial push complete.")
        except Exception as e:
            print(f"Git configuration error: {e}")
            
    else:
        print("Failed to initialize GitHub repository.")

if __name__ == "__main__":
    main()
