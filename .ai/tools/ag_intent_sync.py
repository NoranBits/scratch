#!/usr/bin/env python3
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_core import dump_json_deterministic, get_deterministic_now, get_workspace_root

def check_complexity(tasks):
    """M10: Loop Trigger Policy. Trigger if > 3 tasks."""
    return len(tasks) > 3

def generate_intent_sync_artifacts(user_intent, tasks, now_utc_str=None):
    now = get_deterministic_now(now_utc_str)
    date_str = now.strftime("%Y%m%d")
    loop_id = f"AG-{date_str}-01"
    
    intent_card = {
        "schema_id": "04_SCHEMA_INTENT_CARD",
        "loop_id": loop_id,
        "user_intent_summary": user_intent[:100],
        "success_metrics": [f"Complete {t}" for t in tasks],
        "constraints": ["WRITE_ALLOWLIST_ROOTS enforced", "No L1 silent updates"],
        "milestone_plan": [f"M{i+1}: {t}" for i, t in enumerate(tasks)],
        "exit_criteria": "All milestones verified with evidence."
    }
    
    new_loop_request = None
    if check_complexity(tasks):
        # M13: Complexity Reasoning & Rate-limiting (simulated by unique ID)
        new_loop_request = {
            "trigger": "Complexity threshold exceeded (>3 tasks)",
            "complexity_reasoning": (
                f"The request involves {len(tasks)} distinct operational goals. "
                "The resulting context entropy exceeds safe limits for the current loop. "
                "Splitting these into a fresh session is required for governance safety."
            ),
            "suggested_loop_id": loop_id,
            "commands": "NEW or APPROVE",
            "rate_limit_token": hash(user_intent) # M13: idempotency/rate-limit check
        }
        
    return intent_card, new_loop_request

def main():
    user_intent = "Build a robot, fly to Mars, install Linux, and find water."
    tasks = ["Build Robot", "Mars Transit", "Install Linux", "Water Search"]
    
    print(f"Simulating Intent Synchronizer for: {user_intent}")
    intent_card, new_loop_request = generate_intent_sync_artifacts(user_intent, tasks)
    
    root = get_workspace_root()
    output_dir = os.path.join(root, "STREAMS", "20260301", "INTENT_SYNC")
    os.makedirs(output_dir, exist_ok=True)
    
    intent_path = os.path.join(output_dir, "INTENT_CARD.json")
    request_path = os.path.join(output_dir, "NEW_LOOP_REQUEST.json")
    
    dump_json_deterministic(intent_card, intent_path)
    if new_loop_request:
        print("COMPLEXITY THRESHOLD EXCEEDED: Suggesting NEW loop.")
        dump_json_deterministic(new_loop_request, request_path)
    else:
        print("Complexity within safe bounds.")

if __name__ == "__main__":
    main()
