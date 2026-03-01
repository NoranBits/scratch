import os
import subprocess
import json
import argparse
from datetime import datetime

class AgGitManager:
    """Expert Git Manager for AntiGravity Multi-Agent Systems."""
    
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.external_repos_dir = os.path.join(root_dir, "external_repos")

    def run_command(self, cmd, cwd=None):
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=cwd or self.root_dir, shell=True
            )
            return result.stdout.strip(), result.returncode
        except Exception as e:
            return str(e), 1

    def get_status(self):
        """Returns a summary of the repository status."""
        stdout, code = self.run_command("git status --short")
        if code != 0:
            return {"error": "Failed to get git status"}
        
        lines = stdout.split("\n")
        return {
            "changed_files": [l.strip() for l in lines if l],
            "branch": self.run_command("git branch --show-current")[0]
        }

    def generate_commit_msg(self, loop_id, change_summary, rationale):
        """Generates a semantic commit message per AntiGravity standards."""
        now = datetime.now().isoformat()
        msg = f"[{loop_id}] feat(repo): {change_summary}\n\n"
        msg += f"- Rationale: {rationale}\n"
        msg += f"- Timestamp: {now}\n"
        msg += f"- Manager: AntiGravity Git Agent v1.0"
        return msg

    def commit_changes(self, loop_id, summary, rationale):
        """Stages all changes and commits with generated message."""
        self.run_command("git add .")
        msg = self.generate_commit_msg(loop_id, summary, rationale)
        stdout, code = self.run_command(f'git commit -m "{msg}"')
        return stdout, code

def main():
    parser = argparse.ArgumentParser(description="AntiGravity Git Manager")
    parser.add_argument("--status", action="store_true", help="Show repo status")
    parser.add_argument("--commit", action="store_true", help="Commit all changes")
    parser.add_argument("--loop-id", type=str, help="Active Loop ID")
    parser.add_argument("--msg", type=str, help="Short summary of changes")
    parser.add_argument("--rationale", type=str, help="Rationale for changes")

    args = parser.parse_args()
    manager = AgGitManager(os.getcwd())

    if args.status:
        print(json.dumps(manager.get_status(), indent=2))
    elif args.commit:
        if not all([args.loop_id, args.msg, args.rationale]):
            print("Error: --loop-id, --msg, and --rationale required for commit.")
            return
        out, code = manager.commit_changes(args.loop_id, args.msg, args.rationale)
        print(out)

if __name__ == "__main__":
    main()
