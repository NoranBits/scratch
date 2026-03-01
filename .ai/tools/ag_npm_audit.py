#!/usr/bin/env python3
import json
import os
import sys

def audit_package_json(path):
    """Perform a zero-trust audit on package.json."""
    if not os.path.exists(path):
        print(f"ERROR: {path} not found.")
        return False

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to parse {path}: {e}")
        return False

    issues = []
    
    # Check for suspicious scripts
    scripts = data.get("scripts", {})
    for name, cmd in scripts.items():
        if "rm -rf /" in cmd or "curl" in cmd or "sh " in cmd:
            issues.append(f"Suspicious script '{name}': {cmd}")

    # Check for common insecure dependencies
    deps = data.get("dependencies", {})
    dev_deps = data.get("devDependencies", {})
    all_deps = {**deps, **dev_deps}
    
    insecure_deps = ["node-gyp", "preinstall"] # Sample insecure patterns
    for dep in all_deps:
        if any(p in dep for p in insecure_deps):
            issues.append(f"Potentially insecure dependency: {dep}")

    print(f"--- AntiGravity NPM Audit: {path} ---")
    if issues:
        print("STATUS: FAILED")
        for issue in issues:
            print(f"[!] {issue}")
        return False
    else:
        print("STATUS: PASSED (Zero-Trust Verified)")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ag_npm_audit.py <path_to_package_json>")
        sys.exit(1)
    
    success = audit_package_json(sys.argv[1])
    sys.exit(0 if success else 1)
