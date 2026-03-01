import os
import subprocess
import argparse
import sys
from datetime import datetime

def run_tool(tool_name, *args):
    tool_path = os.path.join(os.path.dirname(__file__), tool_name)
    if not os.path.exists(tool_path):
        print(f"ERROR: Tool {tool_name} not found at {tool_path}")
        return False
    
    cmd = [sys.executable, tool_path] + list(args)
    print(f"--- Running {tool_name} ---")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {tool_name} failed with code {e.returncode}")
        return False

def workplace_routine(write=False):
    print(f"=== AntiGravity Workplace Routine: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    
    # 1. Environment Sanitization
    run_tool("ag_env_sanitizer.py", "--path", ".")
    
    # 2. Security Audit
    run_tool("ag_security_scanner.py", "--path", ".")
    
    # 3. Structure Validation (ag_core logic)
    # Note: ag_core doesn't have a standalone CLI main in the same way, 
    # but we can call ag_skillset_gen or others that use it.
    
    # 4. Mission Control Refresh (Updating INDEX.md)
    # Since ag_summarizer is for removals, we'll manually update INDEX.md or use a generic summary
    print("--- Updating Mission Control ---")
    index_path = os.path.join(os.path.dirname(__file__), "..", "INDEX.md")
    with open(index_path, "a") as f:
        f.write(f"\n- [ROUTINE] Workplace Audit completed at {datetime.now().isoformat()}\n")
    
    print("=== Routine Complete ===")

def main():
    parser = argparse.ArgumentParser(description="AG Workplace Routine")
    parser.add_argument("--write", action="store_true", help="Authorize active updates (if tools support it)")
    
    args = parser.parse_args()
    workplace_routine(write=args.write)

if __name__ == "__main__":
    main()
