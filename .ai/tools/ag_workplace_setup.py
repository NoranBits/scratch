import subprocess
import os
import sys
from pathlib import Path

def run_step(name, cmd, cwd):
    print(f"--- [STEP] {name} ---")
    try:
        result = subprocess.run(cmd, cwd=cwd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"FAILED: {e}")
        print(e.stderr)

def main():
    ROOT = Path(__file__).parent.parent.parent
    TOOLS = ROOT / ".ai" / "tools"
    
    print("Initializing AntiGravity Workplace Setup...")
    
    # Ensure structure
    for d in ["TEMP", "external_repos", ".ai/STATE", ".ai/EVIDENCE"]:
        (ROOT / d).mkdir(parents=True, exist_ok=True)
        
    # 1. Git Pulse
    run_step("Git Pulse Sync", [sys.executable, str(TOOLS / "ag_git_pulse.py")], ROOT)
    
    # 2. Dependency Hoist
    run_step("Dependency Audit", [sys.executable, str(TOOLS / "ag_dep_hoister.py")], ROOT)
    
    # 3. Node/NPM Sync (via Shim)
    if (TOOLS / "ag_npm_shim.py").exists():
        run_step("Node Health Sync", [sys.executable, str(TOOLS / "ag_npm_shim.py"), "sync"], ROOT)
    
    # 4. GPG Security Audit
    if (TOOLS / "ag_gpg_manager.py").exists():
        run_step("Security Audit", [sys.executable, str(TOOLS / "ag_gpg_manager.py")], ROOT)

    # 5. Neural Documentation Generation
    run_step("Neural Refresh", [sys.executable, str(TOOLS / "ag_readme_gen.py")], ROOT)
    
    print("\n[SUCCESS] Workplace Setup Complete. Mission Control updated.")

if __name__ == "__main__":
    main()
