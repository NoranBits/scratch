---
name: diagnostic_integrity
description: Automated verification of repository structure and security constraints.
version: 1.0.0
category: security
---

# Skill: Diagnostic Integrity

This skill provides the Field Agent with the ability to perform deterministic audits of the workplace layout and security enforcement.

## Context (Grounding)
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/01_SECURITY_LAYER.md`.
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/06_WORKPLACE_LAYOUT_LAYER.md`.

## Capabilities
1. **Analyze Workplace**: Use `ag_digest.py` to identify missing control-plane files.
   - **Canonical Audit Targets**:
     - `/.ai/INDEX.md` (Repo Entry)
     - `/.ai/STATE/stable.json` (L1 Anchor)
     - `/.ai/TASKS/active_task.md` (L2 Queue)
     - `/.ai/EVIDENCE/registry.md` (L3 Evidence)
     - `/.ai/DECISIONS/` (Decision Log)
2. **Verify Security**: Periodically test `WRITE_ALLOWLIST_ROOTS` by attempting dry-run writes to `GOVERNANCE/`.
3. **Audit Evidence**: Ensure every file change in `STREAMS/` is linked to a valid `EVID_ID` in `registry.md`.

## Triggers
- Mandatory at the start of every new `loop_id`.
- Triggered by `INTEGRITY_REFACTOR_PATCHSET_REPORT` events.

## Output
- `RETURN_PACKET` with `integrity_report` or `ADAPTER_PROPOSAL` for structural repairs.
