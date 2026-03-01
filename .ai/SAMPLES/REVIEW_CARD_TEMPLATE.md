# PEER REVIEW CARD (TEMPLATE)
**Schema ID**: `04_SCHEMA_REVIEW_CARD_EXTENDED`
**Target ID**: `<DEC-XXXX | TASK-XXXX | DOC-XXXX>`
**Loop ID**: `<LOOP_ID>`

## 1. Reviewer Independence
- **Reviewer Role**: `<independent_agent | council_member | user>`
- **Independence Verified**: `<true | false>` *(Cannot APPROVE if same author)*

## 2. Structured Risk Checklist (Field Agent Expansion)
*The Field Agent must evaluate these technical constraints before returning a verdict.*

- [ ] **Security Layer Check (01)**: Do the changes violate `WRITE_ALLOWLIST_ROOTS` or alter L0/L1 state silently?
- [ ] **Determinism Check**: Are outputs byte-stable (e.g., sort_keys=True, fixed UTC offsets)?
- [ ] **Rollback Capability**: Is there a clear path to undo these changes if they degrade the workspace?
- [ ] **Test Coverage**: Does the Return Packet contain passing negative/positive test proofs?

## 3. Evidence Status
- **Validated Evidence ID(s)**: `<EVID:...>`
- **Disputed / Missing Evidence**: `<EVID:... or N/A>`

## 4. Verdict
- **Verdict**: `<APPROVE | REVISE | REJECT>`
- **Enforcement Required**: `<true | false>`
- **Required Actions**:
  - [P0] `<Mandatory change before passing>`
  - [P1] `<Recommended change>`
