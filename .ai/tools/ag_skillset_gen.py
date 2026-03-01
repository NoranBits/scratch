#!/usr/bin/env python3
import os
import json
import argparse
import sys
from datetime import datetime

# M16: Policy alignment - replacing pathlib/re with os/json/datetime
# Ensuring [ROOT] policy and safe-mode by default.

def get_workspace_root():
    """Canonical root discovery."""
    current = os.path.abspath(os.path.dirname(__file__))
    # Look for .ai directory to signify root
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, ".ai")):
            return current
        current = os.path.dirname(current)
    return os.path.abspath(os.getcwd())

def generate_skillset(name, description, skills, output_filename, dry_run=True):
    root = get_workspace_root()
    skillsets_dir = os.path.join(root, ".ai", "SKILLSETS")
    
    # M16: Enforce write allowlist root
    target_path = os.path.join(skillsets_dir, output_filename)
    
    skillset = {
        "skillset_id": f"SKSET-{datetime.now().strftime('%Y%p%d-%H%M')}",
        "name": name,
        "description": description,
        "skills": skills,
        "author": "AntiGravity (Automated)",
        "created_at": datetime.now().isoformat()
    }
    
    content = json.dumps(skillset, indent=2)
    
    print(f"--- Skillset Generation ---")
    print(f"Target: {target_path}")
    print(f"Mode: {'DRY RUN (Safe)' if dry_run else 'WRITE (Active)'}")
    print(f"Content:\n{content}")
    
    if not dry_run:
        if not os.path.exists(skillsets_dir):
            os.makedirs(skillsets_dir, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"SUCCESS: Skillset written to {target_path}")
        print(f"Loop ID: AG-{datetime.now().strftime('%Y%m%d')}-01 | STATUS: ACTIVE")
    else:
        print("\n[!] SAFE MODE: No changes were made to the file system.")
        print("[!] ACTION REQUIRED: Use --write flag to authorize active repository updates.")

def scaffold_project(project_type, root):
    """Create basic structure for JS/TS projects."""
    if project_type not in ["js", "ts"]:
        print(f"ERROR: Unsupported project type {project_type}")
        return

    print(f"--- Scaffolding {project_type.upper()} Project ---")
    
    # package.json template
    pkg = {
        "name": "ag-field-project",
        "version": "1.0.0",
        "private": true,
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1",
            "audit": "python .ai/tools/ag_npm_audit.py package.json"
        },
        "dependencies": {},
        "devDependencies": {}
    }
    
    with open(os.path.join(root, "package.json"), "w") as f:
        json.dump(pkg, f, indent=2)
    
    # Create src directory
    os.makedirs(os.path.join(root, "src"), exist_ok=True)
    
    if project_type == "ts":
        tsconfig = {
            "compilerOptions": {
                "target": "ES6",
                "module": "commonjs",
                "outDir": "./dist",
                "strict": true,
                "esModuleInterop": true
            }
        }
        with open(os.path.join(root, "tsconfig.json"), "w") as f:
            json.dump(tsconfig, f, indent=2)
        print("Created tsconfig.json")

    print("SUCCESS: Project scaffolded.")

def main():
    parser = argparse.ArgumentParser(description="AG Skillset Generator v1.2 (Node.js Support)")
    parser.add_argument("--name", help="Skillset name")
    parser.add_argument("--desc", default="", help="Skillset description")
    parser.add_argument("--skills", nargs='+', help="List of skill IDs or paths")
    parser.add_argument("--output", default="new_skillset.json", help="Output filename")
    parser.add_argument("--write", action="store_true", help="Explicitly authorize write operation")
    parser.add_argument("--scaffold", choices=["js", "ts"], help="Scaffold a new project")
    
    args = parser.parse_args()
    root = get_workspace_root()

    if args.scaffold:
        if args.write:
            scaffold_project(args.scaffold, root)
        else:
            print("[!] SAFE MODE: Scaffolding requires --write flag.")
        return

    if not args.name or not args.skills:
        parser.print_help()
        return
    
    skills_list = []
    for s in args.skills:
        skills_list.append({"id": s, "path": f"[ROOT]/.ai/SKILLS/{s}.md"})
        
    generate_skillset(
        name=args.name,
        description=args.desc,
        skills=skills_list,
        output_filename=args.output,
        dry_run=not args.write
    )

if __name__ == "__main__":
    main()
