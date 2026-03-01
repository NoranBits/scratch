#!/usr/bin/env python3
import sys
import os
import argparse
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_core import (
    dump_json_deterministic, 
    get_deterministic_now, 
    get_workspace_root,
    check_write_permission
)

def load_harmonization_rules():
    root = get_workspace_root()
    rules_path = os.path.join(root, ".ai", "tools", "HARMONIZATION_RULES.json")
    if os.path.exists(rules_path):
        with open(rules_path, "r") as f:
            return json.load(f)
    return {"EXCLUDE_PATHS": [], "FORBIDDEN_TRANSFORMS": {}}

def generate_adapter_proposal(digest_report_path: str, chunk_id: str, now_utc_str: str = None):
    # M4: ADAPTER_PROPOSAL generator
    now = get_deterministic_now(now_utc_str)
    date_str = now.strftime("%Y%m%d")
    
    workspace = get_workspace_root()
    output_dir = os.path.join(workspace, "STREAMS", date_str, chunk_id)
    
    # Read dummy source report or real one if exists
    source_evids = []
    if digest_report_path and os.path.exists(digest_report_path):
        try:
            with open(digest_report_path, "r", encoding="utf-8") as f:
                report = json.load(f)
                source_evids = report.get("related_evids", ["EVID:UNSPECIFIED"])
        except Exception:
            source_evids = ["EVID:UNSPECIFIED"]
    else:
        source_evids = [f"EVID:DOC:{date_str}:0000"]
            
    proposal_json_path = os.path.join(output_dir, "ADAPTER_PROPOSAL.json")
    proposal_md_path = os.path.join(output_dir, "ADAPTER_PROPOSAL.md")
    review_stub_path = os.path.join(output_dir, f"REVIEW_CARD_{proposal['proposal_id']}.md")
    
    rules = load_harmonization_rules()
    exclude_list = ", ".join(rules.get("EXCLUDE_PATHS", []))
    
    proposal = {
        "proposal_id": f"PROP-{date_str}-{chunk_id}",
        "source_digest_evid_ids": source_evids,
        "capability_changes": [
            {
                "name": "KB Harmonization Adapter",
                "rationale": f"Enforcing ROOT_POLICY. Excluded paths: {exclude_list}. Forbidden transforms applied to command tokens and governance fields.",
                "risk": "LOW",
                "tests": "ag_digest.py structural audit",
                "rollback": "L1 State Anchor Restore"
            }
        ],
        "requires_manual_validation": True,
        "requested_write_targets": [
            f"STREAMS/{date_str}/{chunk_id}/output.json"
        ]
    }

    print(f"Generating proposal at {proposal_json_path}")
    dump_json_deterministic(proposal, proposal_json_path)

    check_write_permission(proposal_md_path)
    md_content = f"""# ADAPTER PROPOSAL
**ID**: {proposal['proposal_id']}
**Requires Manual Validation**: {proposal['requires_manual_validation']}

## Capability Changes
"""
    for cap in proposal['capability_changes']:
        md_content += f"- **{cap['name']}**: {cap['rationale']} (Risk: {cap['risk']})\n"
        
    with open(proposal_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    # M12: REVIEW_CARD stub
    check_write_permission(review_stub_path)
    review_content = f"""# REVIEW_CARD (STUB)
**Target ID**: {proposal['proposal_id']}
**Loop ID**: {now.strftime("AG-%Y%m%d-01")}
**Status**: PENDING_AUDIT

## Structured Evaluation
- [ ] **Security Layer Check**: Validated against allowlist?
- [ ] **Determinism Check**: Byte-stable?
- [ ] **Rollback**: Path to undo?

**Verdict**: PENDING
"""
    with open(review_stub_path, "w", encoding="utf-8") as f:
        f.write(review_content)
        
    print(f"Generated Review Card stub at {review_stub_path}")
    
def main():
    parser = argparse.ArgumentParser(description="AG Adapter Gen Tool")
    parser.add_argument("--report", required=False, help="Path to input digest report")
    parser.add_argument("--chunk", required=True, help="Chunk ID (e.g. CHUNK_01)")
    parser.add_argument("--now-utc", help="Deterministic timestamp in ISO format")
    
    args = parser.parse_args()
    
    generate_adapter_proposal(args.report, args.chunk, args.now_utc)

if __name__ == "__main__":
    main()
