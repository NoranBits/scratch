# CAPABILITY PROMOTION: diagnostic_integrity
**Schema**: `07_SCHEMA_CAPABILITY_PROMOTION`

## Tool Identifier
- **Skill Name / ID**: `diagnostic_integrity`
- **Current Status**: VERIFY
- **Target Status**: FACT

## Test Execution Evidence (MUST)
- **Test Description**: Verified canonical audit targets and security block invariants.
- **Execution Log**: [smoke_test_report.md](./.ai/STREAMS/20260301/smoke_test_report.md)
- **EVID_ID Reference**: `EVID:TEST:20260301:DIAG_PASS`, `EVID:TEST:20260301:SEC_DENY`

## Canonical Audit Targets (Structural)
The following files must be present and byte-stable for a successful audit:
1. `[ROOT]/.ai/INDEX.md`
2. `[ROOT]/.ai/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md`
3. `[ROOT]/.ai/tools/ag_core.py`
4. `[ROOT]/.ai/tools/ag_digest.py`
5. `[ROOT]/.ai/STATE/active_snapshot.json`

## Rollback & Risk Assessment
- **Failure Mode**: False positive on integrity checks.
- **Rollback Strategy**: Manual review of `ag_digest.py` output; restore from L1 state anchor.

## Governance Approval
- **Validation Method**: test_and_log_review
- **Promoted By**: AntiGravity (Intent Synchronizer)
- **Date Promoted**: 2026-03-01T21:18:00Z
