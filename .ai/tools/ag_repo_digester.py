import os
import shutil
import json
import argparse
from datetime import datetime

class AgRepoDigester:
    """Automated tool for selectively digesting components from forked repositories."""
    
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.manifest_path = os.path.join(root_dir, ".ai", "FEDERATION", "digestion_manifest.json")
        self._ensure_manifest()

    def _ensure_manifest(self):
        os.makedirs(os.path.dirname(self.manifest_path), exist_ok=True)
        if not os.path.exists(self.manifest_path):
            with open(self.manifest_path, 'w') as f:
                json.dump({"digested_components": []}, f, indent=4)

    def digest(self, source_path, target_path, source_repo_url, commit_hash):
        """Extracts a path and registers it in the manifest."""
        abs_source = os.path.join(self.root_dir, source_path)
        abs_target = os.path.join(self.root_dir, target_path)
        
        if not os.path.exists(abs_source):
            return f"Error: Source path {source_path} not found.", 1

        # Perform the extraction
        os.makedirs(os.path.dirname(abs_target), exist_ok=True)
        if os.path.isdir(abs_source):
            if os.path.exists(abs_target):
                shutil.rmtree(abs_target)
            shutil.copytree(abs_source, abs_target)
        else:
            shutil.copy2(abs_source, abs_target)

        # Register in manifest
        with open(self.manifest_path, 'r+') as f:
            data = json.load(f)
            data["digested_components"].append({
                "source": source_path,
                "target": target_path,
                "upstream": source_repo_url,
                "commit": commit_hash,
                "timestamp": datetime.now().isoformat()
            })
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            
        return f"Successfully digested {source_path} into {target_path}", 0

def main():
    parser = argparse.ArgumentParser(description="AntiGravity Repository Digester")
    parser.add_argument("--source", type=str, required=True, help="Path in external_repos/")
    parser.add_argument("--target", type=str, required=True, help="Local target path")
    parser.add_argument("--upstream", type=str, required=True, help="Source repo URL")
    parser.add_argument("--commit", type=str, required=True, help="Source commit hash")

    args = parser.parse_args()
    digester = AgRepoDigester(os.getcwd())
    msg, code = digester.digest(args.source, args.target, args.upstream, args.commit)
    print(msg)

if __name__ == "__main__":
    main()
