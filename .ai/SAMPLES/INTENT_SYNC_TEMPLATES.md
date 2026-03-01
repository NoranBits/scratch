# INTENT CARD (TEMPLATE)
**Schema ID**: `04_SCHEMA_INTENT_CARD`
**Loop ID**: `<NEW_LOOP_ID>`

## 1. User Intent Summary
- **Primary Goal**: `<Extracted high-level goal from user prompt>`
- **SMART Success Metrics**:
  - [ ] `<Metric 1: Measurable outcome>`
  - [ ] `<Metric 2: Verification command/result>`

## 2. Planning Pack
- **Milestones**:
  - `M1`: Reconnaissance
  - `M2`: ...
- **Exit Criteria**: `<Specific condition for loop closure>`

---

# NEW LOOP REQUEST (TEMPLATE)
**Trigger**: Complexity threshold exceeded (>3 independent tasks / High risk).

## Request
"AntiGravity and the Orchestrator have detected significant complexity in your request. To maintain context integrity and structural safety, we recommend initiating a new dedicated loop."

- **Reasoning**: `<Complexity analysis bullet points>`
- **Javasolt Loop ID**: `AG-YYYYMMDD-XX`
- **Commands**: 
  - Reply with **`NEW`** to authorize the loop jump.
  - Reply with **`APPROVE`** to force continuation in the current loop.
