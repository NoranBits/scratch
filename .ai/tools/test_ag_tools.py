#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_core import (
    is_path_allowed, 
    check_write_permission, 
    get_workspace_root,
    dump_json_deterministic
)

def main():
    root = get_workspace_root()
    packet = {
        "executed_commands": [],
        "now_utc_used": True,
        "outputs_created": [],
        "tests_run": [],
        "deviations_risks": []
    }
    
    # Test 1: Negative Test (M1)
    try:
        protected_target = os.path.join(root, "GOVERNANCE", "test.json")
        check_write_permission(protected_target)
        packet["tests_run"].append({"name": "M1 Negative Test (GOVERNANCE)", "status": "FAIL - Allowed write"})
    except PermissionError as e:
        packet["tests_run"].append({"name": "M1 Negative Test (GOVERNANCE)", "status": f"PASS - DENIED: {e}"})

    # Test 2: Verify Command & Bootstrap (M2 & M3)
    try:
        result = subprocess.run([sys.executable, "ag_digest.py", "verify"], 
                                cwd=os.path.dirname(os.path.abspath(__file__)),
                                capture_output=True, text=True)
        packet["executed_commands"].append("ag_digest.py verify")
        if "Missing" in result.stdout or "Present" in result.stdout:
            packet["tests_run"].append({"name": "M3 Verify Command", "status": "PASS - Generated report"})
            # Check bootstrap M2
            config_path = os.path.join(root, "STREAMS", "_config", "protected_paths.json")
            if os.path.exists(config_path):
                packet["tests_run"].append({"name": "M2 Bootstrap", "status": "PASS"})
                packet["outputs_created"].append(config_path)
            else:
                packet["tests_run"].append({"name": "M2 Bootstrap", "status": "FAIL - Config not found"})
        else:
            packet["tests_run"].append({"name": "M3 Verify Command", "status": f"FAIL - Unexpected output: {result.stdout}"})
    except Exception as e:
         packet["tests_run"].append({"name": "M3 Verify Command", "status": f"FAIL - Error: {e}"})

    # Test 3: Adapter Gen (M4 & M5)
    try:
        now_utc = "2026-03-01T15:00:00Z"
        result = subprocess.run(
            [sys.executable, "ag_adapter_gen.py", "--chunk", "CHUNK_01", "--now-utc", now_utc],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True, text=True
        )
        packet["executed_commands"].append(f"ag_adapter_gen.py --chunk CHUNK_01 --now-utc {now_utc}")
        
        output_dir = os.path.join(root, "STREAMS", "20260301", "CHUNK_01")
        json_path = os.path.join(output_dir, "ADAPTER_PROPOSAL.json")
        md_path = os.path.join(output_dir, "ADAPTER_PROPOSAL.md")
        
        if os.path.exists(json_path) and os.path.exists(md_path):
            packet["tests_run"].append({"name": "M4 & M5 Proposal Emitter", "status": "PASS"})
            packet["outputs_created"].extend([json_path, md_path])
        else:
            packet["tests_run"].append({"name": "M4 & M5 Proposal Emitter", "status": "FAIL - Artifacts missing"})
            
    except Exception as e:
         packet["tests_run"].append({"name": "M4 & M5 Proposal Emitter", "status": f"FAIL - Error: {e}"})

    # Write RETURN_PACKET
    packet_path = os.path.join(root, "STREAMS", "RETURN_PACKET.json")
    try:
        dump_json_deterministic(packet, packet_path)
        print(f"Created RETURN_PACKET.json successfully at {packet_path}")
    except Exception as e:
        print(f"Failed to create RETURN_PACKET: {e}")

if __name__ == "__main__":
    main()
