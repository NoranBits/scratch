# CAPABILITY PROMOTION EVIDENCE: STEP C
**Loop ID**: AG-20260301-02
**Date**: 2026-03-01

## 1. Tool: `ag_summarizer.py`
- **Current Status**: VERIFY
- **Target Status**: FACT
- **Test Evidence (M11)**:
  - **Input**: `TEMP/test_summarizer_input.md` containing 3 EVIDs.
  - **Execution**: `python ag_summarizer.py TestItem "Summary" input.md`
  - **Result**: Successfully extracted `EVID:DOC:20260301:9991`, `EVID:TEST:20260301:9992`, `EVID:CODE:20260301:9993`.
  - **Output**: `ARCHIVE/summaries/removed_testitem.json` (Deterministic).
- **Verdict**: **PROMOTE TO FACT**.

## 2. Tool: `ag_intent_sync.py`
- **Current Status**: VERIFY
- **Target Status**: FACT
- **Test Evidence (M11)**:
  - **Positive Test (High Complexity)**: Input 4 tasks. Output: `NEW_LOOP_REQUEST.json` generated.
  - **Negative Test (Low Complexity)**: Input 1 task. Output: Complexity within safe bounds (No NEW loop).
- **Verdict**: **PROMOTE TO FACT**.

## 3. Tool: `ag_core.py` (Security Invariant)
- **Test Evidence**: 
  - Attempted unauthorized write to `removed_testitem.json` at root.
  - **Result**: `PermissionError: DENY = Path removed_testitem.json is outside of WRITE_ALLOWLIST_ROOTS.`
- **Verdict**: **VERIFIED FACT**.
