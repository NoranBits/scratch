# PROMOTION CARD: diagnostic_integrity
**ID**: AG-PROM-20260301-DIAG
**Loop ID**: AG-20260301-01

## Capability Status
- **Source Status**: VERIFY
- **Target Status**: FACT
- **Trust Domain**: Orchestrator Core

## Evidence Links
- **Audit Targets**: [PROMOTION_DIAGNOSTIC_INTEGRITY.md](./.ai/EVIDENCE/PROMOTION_DIAGNOSTIC_INTEGRITY.md)
- **Harmonization Rules**: [HARMONIZATION_RULES.json](./.ai/tools/HARMONIZATION_RULES.json)
- **Safe-Mode Generator**: `ag_skillset_gen.py` (v1.1.1)

## Summary of Improvements
1.  **Safe-by-Default**: Generator now enforces `--write` flag and provides deterministic loop logs.
2.  **Harmonization Rules**: Strict exclusion list (STREAMS/, ARCHIVE/) implemented.
3.  **Canonical Audit**: Established byte-stable targets for recursive integrity checks.

## Verdict
**PROMOTED TO FACT**
*Authorized by AntiGravity (Intent Synchronizer)*
*2026-03-01T21:46:00Z*

## Knowledge Map
- **Governance**: [Harmonization Rules](./.ai/tools/HARMONIZATION_RULES.json)
- **Integrity**: [Diagnostic Evidence](./.ai/EVIDENCE/PROMOTION_DIAGNOSTIC_INTEGRITY.md)
- **Deployment**: [Skillset Generator](./.ai/tools/ag_skillset_gen.py)
