---
name: kb_harmonization
description: Enforcing ROOT_POLICY across all Knowledge Base layers.
version: 1.1.0
category: governance
---

# Skill: KB Harmonization

This skill ensures that all repository documentation adheres to the `AI_FOLDER_ALLOW_FALLBACK` protocol and uses `[ROOT]/` as the canonical path variable.

## Context (Grounding)
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md`.
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/04_GOVERNANCE_INTERFACE_PACK.md`.
- Reference `INTEGRITY_REFACTOR_PATCHSET_REPORT.md`.

## Capabilities
1. **Path Normalization**: Scan `.md` files in `knowledge/` for hardcoded `/.ai/` paths and propose `[ROOT]/` replacements.
   - **Exclude Paths**: `STREAMS/`, `ARCHIVE/`, `_generated/`, `node_modules/`, `build/`.
2. **Schema Audit**: Verify that `HANDOFF_MANIFEST` and `DECISION_CARD` files use absolute pathing logic defined in Layer 06.
3. **Prompt Alignment**: Refactor internal guidance to use AI-agnostic terminology.
   - **Forbidden Transforms**:
     - DO NOT modify Command Guard tokens (`NEW`, `APPROVE`, etc.).
     - DO NOT refactor `loop_id` fields in active snapshots.
     - DO NOT update `TRUST_LEVEL=FACT` without evidence.

## Workflow
- Scan → Propose Adapter → Sync with Orchestrator → Execute after approval.
