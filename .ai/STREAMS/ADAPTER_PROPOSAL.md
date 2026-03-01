# ADAPTER PROPOSAL
**ID**: PROP-20260301-KB-REVALUATION
**Source Digest**: EVID:DOC:20260301:REVAL
**Requires Manual Validation**: True

## Objective
Align the repository's Knowledge Base (KB) and governance layout strictly with `INTEGRITY_REFACTOR_PATCHSET_REPORT.md` and Layer 06's `ROOT_POLICY`. Eliminate any remaining `/.ai/` hardcoded paths in constitutional files and map external repository structures.

## Capability Changes & Required Updates

1. **Update `00_PROTOCOL_LAYER.md` (Risk: LOW)**
   - *Rationale*: Section 6 "TRACE-FIRST GOVERNANCE" hardcodes `/.ai/` as the repo structure. 
   - *Change*: Replace `/.ai/` with `[ROOT]/` to comply with the ROOT_POLICY fallback capabilities outlined in Layer 06.

2. **Update `04_GOVERNANCE_INTERFACE_PACK.md` (Risk: LOW)**
   - *Rationale*: While DECISION_CARD paths were successfully patched to `[ROOT]/GOVERNANCE/...`, the `REVIEW_CARD` and `HANDOFF_MANIFEST` schemas still hardcode `/.ai/REVIEWS/` and `/.ai/HANDOFFS/`.
   - *Change*: Patch these schema path references to `[ROOT]/GOVERNANCE/reviews/` and `[ROOT]/HANDOFFS/` or `[ROOT]/GOVERNANCE/handoffs/` depending on Layer 06 (Layer 06 says `[ROOT]/HANDOFFS/`).

3. **External Repo Alignment: `repo_alpha` (Risk: MEDIUM)**
   - *Rationale*: Discovered `repo_alpha/.ai/FEDERATION/peers.md`.
   - *Change*: Ensure that federation templates and peer governance in external repositories inherit properly from the central Orchestrator instructions without violating the Single Source of Truth rule. For now, acknowledge the existence and treat `repo_alpha` as a satellite with its own `[ROOT]` context.

## Actions to Execute
- `sed` or `multi_replace` across the specific KB files to finalize the patches.
- No files to rename at this time, since the `[ROOT]` alias allows `/.ai/` to function normally. We just need the *documentation* to be agnostic.
