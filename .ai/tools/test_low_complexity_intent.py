#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_intent_sync import generate_intent_sync_artifacts

def test_low_complexity():
    user_intent = "Fix a typo in the README."
    tasks = ["Fix typo"]
    
    print(f"Simulating LOW complexity for: {user_intent}")
    intent_card, new_loop_request = generate_intent_sync_artifacts(user_intent, tasks)
    
    if new_loop_request:
        print("FAIL: Triggered NEW loop on low complexity.")
    else:
        print("PASS: Complexity within safe bounds (No NEW loop suggested).")

if __name__ == "__main__":
    test_low_complexity()
