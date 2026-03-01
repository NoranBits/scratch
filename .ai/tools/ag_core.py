import os
import datetime
import json
import logging
from pathlib import Path

# Hard-coded WRITE_ALLOWLIST_ROOTS (P0 security invariant)
WRITE_ALLOWLIST_ROOTS = [
    "STREAMS",
    "ARCHIVE",
    "TEMP",
    "EVIDENCE",
    "TASKS"
]

def get_workspace_root() -> str:
    """Returns the .ai root directory heuristically based on this script's location."""
    # Assuming tools/ag_core.py -> root is .ai/
    return str(Path(__file__).parent.parent.absolute())

def is_path_allowed(workspace_root: str, target_path: str, allowlist_roots: list = WRITE_ALLOWLIST_ROOTS) -> bool:
    """
    M1: Hard enforcement of WRITE_ALLOWLIST_ROOTS.
    Checks if the target_path, after realpath normalization, falls strictly under one of the allowed roots.
    """
    workspace_real = os.path.realpath(workspace_root)
    target_real = os.path.realpath(target_path)
    
    for allowed_rel in allowlist_roots:
        allowed_real = os.path.realpath(os.path.join(workspace_real, allowed_rel))
        # Prefix check to ensure it falls under the allowed directory
        if target_real.startswith(allowed_real + os.sep) or target_real == allowed_real:
            return True
            
    return False

def check_write_permission(target_path: str):
    """Throws PermissionError if path is not in allowlist."""
    if not is_path_allowed(get_workspace_root(), target_path):
        raise PermissionError(f"DENY = Path {target_path} is outside of WRITE_ALLOWLIST_ROOTS.")

def get_deterministic_now(now_utc_str: str = None) -> datetime.datetime:
    """M5: Provides deterministic UTC times."""
    if now_utc_str:
        try:
            return datetime.datetime.fromisoformat(now_utc_str.replace("Z", "+00:00"))
        except ValueError:
            pass
    return datetime.datetime.now(datetime.timezone.utc)

def dump_json_deterministic(data, filepath: str):
    """M5: byte-stabil output: sort_keys=True"""
    check_write_permission(filepath)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")

def check_bootstrap_config() -> dict:
    """M2: First-run bootstrap of protected_paths.json"""
    root = get_workspace_root()
    config_dir = os.path.join(root, "STREAMS", "_config")
    config_path = os.path.join(config_dir, "protected_paths.json")
    
    default_config = {
        "protected": ["GOVERNANCE", "HANDOFFS", "STABLE_STATE", "PROTOCOL", "LAYER_00_09"],
        "description": "Diagnostic reference list of protected governance paths."
    }
    
    if not os.path.exists(config_path):
        logging.info("Bootstrapping protected_paths.json for the first time...")
        dump_json_deterministic(default_config, config_path)
        return default_config
        
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_workplace_verify() -> dict:
    """M3: verify subcommand: workplace drift report + config presence"""
    root = get_workspace_root()
    config = check_bootstrap_config()
    
    report = {
        "status": "PASS",
        "missing": [],
        "present": []
    }
    
    for relative_path in config.get("protected", []):
        full_path = os.path.join(root, relative_path)
        if not os.path.exists(full_path):
            report["missing"].append(relative_path)
            report["status"] = "WARN - Integrity drift detected"
        else:
            report["present"].append(relative_path)
            
    return report
