import subprocess
import sys
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

class ReleaseNexus:
    def __init__(self, root_path):
        self.root = Path(root_path)

    def run_git(self, args):
        result = subprocess.run(["git"] + args, cwd=self.root, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Git Error: {' '.join(args)}")
            print(result.stderr)
            return None
        return result.stdout.strip()

    def get_current_branch(self):
        return self.run_git(["rev-parse", "--abbrev-ref", "HEAD"])

    def audit_phases(self):
        print("\n--- [RELEASE NEXUS] Phase Audit ---")
        current = self.get_current_branch()
        print(f"Active Branch: {current}")
        
        for i in range(len(PHASES) - 1):
            upstream = PHASES[i]
            downstream = PHASES[i+1]
            
            diff_count = self.run_git(["rev-list", "--count", f"{downstream}..{upstream}"])
            if diff_count is not None:
                status = "SYNCHRONIZED" if diff_count == "0" else f"AHEAD BY {diff_count} COMMITS"
                print(f"[{upstream}] -> [{downstream}]: {status}")

    def promote(self, target_phase):
        if target_phase not in PHASES:
            print(f"Error: Invalid phase '{target_phase}'.")
            return

        idx = PHASES.index(target_phase)
        if idx == 0:
            print("Error: Cannot promote to 'dev' (it is the root phase).")
            return

        upstream = PHASES[idx - 1]
        print(f"Starting promotion: [{upstream}] -> [{target_phase}]")

        # 1. Checkout target
        self.run_git(["checkout", target_phase])
        
        # 2. Merge upstream
        msg = f"chore(release): promote phase {upstream} to {target_phase} [via ag_release_nexus]"
        merge_result = self.run_git(["merge", upstream, "-m", msg, "-S"]) # -S for GPG signing
        
        if merge_result is not None:
            print(f"[SUCCESS] Phase {target_phase} updated.")
            # 3. Push
            self.run_git(["push", "origin", target_phase])
        
        # Return to dev or previous
        self.run_git(["checkout", "dev"])

def main():
    nexus = ReleaseNexus(Path(__file__).parent.parent)
    
    if len(sys.argv) < 2:
        nexus.audit_phases()
        print("\nUsage:")
        print("  python ag_release_nexus.py promote [phase_name]")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "promote" and len(sys.argv) == 3:
        nexus.promote(sys.argv[2])
    else:
        nexus.audit_phases()

if __name__ == "__main__":
    main()
