import os
import subprocess
import sys
from pathlib import Path

# --- CONFIGURATION ---
# Found node binary path from previous search
NODE_PATH = r"C:\Users\nono\AppData\Local\ms-playwright-go\1.50.1\node.exe"

def run_node(script_path, *args):
    if not os.path.exists(NODE_PATH):
        print(f"Error: Node binary not found at {NODE_PATH}")
        return False
    
    cmd = [NODE_PATH, script_path] + list(args)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python ag_npm_shim.py <script_name> [args]")
        print("Example: python ag_npm_shim.py sync")
        return

    action = sys.argv[1]
    
    # Simple mapping of "npm run" commands
    if action == "sync":
        run_node(".ai/tools/ag_node_sync.js")
    elif action == "audit":
        run_node(".ai/tools/ag_dep_checker.js")
    elif action == "test":
        print("Executing simulated test suite...")
    else:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    main()
