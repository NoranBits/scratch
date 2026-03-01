#!/usr/bin/env python3
import sys
import os
import json
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_core import dump_json_deterministic, get_deterministic_now, get_workspace_root

def extract_evids(text):
    """Finds all EVID_IDs in a block of text."""
    return sorted(list(set(re.findall(r"EVID:[A-Z]+:\d{8}:\d{4}", text))))

def generate_removal_summary(item_name, original_content, summary_text, now_utc_str=None):
    """
    M8: Summarize-Removed Mechanism.
    Creates a deterministic summary of removed content while preserving EVID_IDs.
    """
    evids = extract_evids(original_content)
    now = get_deterministic_now(now_utc_str)
    
    summary_packet = {
        "item_name": item_name,
        "removed_at_utc": now.isoformat(),
        "summary": summary_text,
        "preserved_evid_ids": evids,
        "format_version": "1.0.0"
    }
    
    return summary_packet

def main():
    if len(sys.argv) < 3:
        print("Usage: ag_summarizer.py <item_name> <summary_text> [file_path]")
        sys.exit(1)
        
    item_name = sys.argv[1]
    summary_text = sys.argv[2]
    
    original_content = ""
    if len(sys.argv) > 3 and os.path.exists(sys.argv[3]):
        with open(sys.argv[3], "r", encoding="utf-8") as f:
            original_content = f.read()
            
    summary = generate_removal_summary(item_name, original_content, summary_text)
    
    # Using ag_core's deterministic dump
    root = get_workspace_root()
    output_dir = os.path.join(root, "ARCHIVE", "summaries")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"removed_{item_name.lower().replace(' ', '_')}.json")
    print(f"Generating deterministic summary for {item_name} with {len(summary['preserved_evid_ids'])} EVIDs.")
    dump_json_deterministic(summary, output_path)

if __name__ == "__main__":
    main()
