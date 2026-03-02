import json
import os
from pathlib import Path

def hoist_dependencies(root):
    """
    Analyzes all package.json files in the workspace to identify shared dependencies.
    """
    registry = {
        "shared": {},
        "conflicts": [],
        "projects_scanned": 0
    }
    
    # Root package.json
    root_pkg_path = root / "package.json"
    if root_pkg_path.exists():
        with open(root_pkg_path, "r") as f:
            data = json.load(f)
            registry["shared"].update(data.get("dependencies", {}))
            registry["shared"].update(data.get("devDependencies", {}))
            registry["projects_scanned"] += 1

    # Check external_repos
    external = root / "external_repos"
    if external.exists():
        for repo_dir in external.iterdir():
            if repo_dir.is_dir():
                pkg = repo_dir / "package.json"
                if pkg.exists():
                    with open(pkg, "r") as f:
                        data = json.load(f)
                        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                        for name, version in deps.items():
                            if name in registry["shared"] and registry["shared"][name] != version:
                                registry["conflicts"].append({
                                    "package": name,
                                    "root_version": registry["shared"][name],
                                    "repo": repo_dir.name,
                                    "version": version
                                })
                            else:
                                registry["shared"][name] = version
                    registry["projects_scanned"] += 1
    
    return registry

if __name__ == "__main__":
    ROOT = Path(__file__).parent.parent.parent
    report = hoist_dependencies(ROOT)
    
    output_path = ROOT / ".ai" / "dep_hoist_audit.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"Dependency hoisting audit complete. Scanned {report['projects_scanned']} projects.")
    if report["conflicts"]:
        print(f"WARNING: Found {len(report['conflicts'])} version conflicts.")
