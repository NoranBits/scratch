# FIELD AGENT GUIDE: Understanding the In-App Orchestrator Architecture

This document serves to enhance the capabilities of the Field Agent (e.g., Anti-Gravity Agent) by providing a deep understanding of how external in-app orchestrators (like `chatgpt_orchestrator`) generate their outputs and enforce governance.

## 1. The Strict Protocol Layer (Layer 00)
External orchestrators operate under a highly rigid, deterministic protocol.
- **First Line Rule**: Every output begins exactly with `1. Megértés és Kontextus (State Anchor)`. There is no preamble.
- **Language Firewall**: Steps 1-7 are processed in Hungarian for internal reasoning and governance, while Step 8 (Deliverables) is output in English for execution.
- **APPROVE ≠ EXECUTE**: Orchestrators cannot modify the repository directly. They can only formulate `DECISION_CARD`s and grant `APPROVE` status. Actual file modifications require an explicit `HANDOFF_MANIFEST` to the Field Agent.

## 2. Context Architecture (Layer 02)
Orchestrators load context in a strict hierarchy to prevent "drift" and hallucinations:
- **L0 (Canon)**: Immutable rules (Protocol, Security).
- **L1 (Stable State Anchor)**: The current, approved truth (`stable_state.md`).
- **L2 (Active Task Context)**: Short-term operational focus (`active_task.md`).
- **L3 (Evidence Graph)**: Validated facts and references (`registry.md`). 
*Note for Field Agent: Your outputs (Return Contracts) are the primary source for promoting items from `VERIFY` to `FACT` in L3.*

## 3. Governance and Handoffs (Layers 04 & 05)
The orchestrator cannot "just do things." It must navigate gates:
- **Governance (L4)**: Structural changes require a `DECISION_CARD`. 
- **Routing & Execution (L5)**: When the orchestrator determines an action needs taking (writing code, running tests, web research), it creates a `HANDOFF_MANIFEST`.
- **Your Role as Field Agent**: When you receive a `HANDOFF_MANIFEST`, you are the executor. You *must* return a precise **Return Contract** (list of updated files, EVID_IDs, execution summary). If you fail to return a complete contract, the orchestrator gets stuck in a `SYNC_REQUIRED` state and cannot update L1.

## 4. Tooling and Capabilities (Layer 07)
The orchestrator maintains a model of what you (the Field Agent) can do.
- **Capability IDs (CAP)**: e.g., `CAP:REPO:READ_TREE`, `CAP:SEARCH:WEB`.
- **Trust Levels**: Tools default to `VERIFY` unless explicitly proven by an `Adapter Card` or validation step to be `FACT`.
- **Implication**: Do not claim you have a capability without proving it. If the orchestrator assigns you a task with a `VERIFY` tool, your first step is to execute and return evidence that the tool worked successfully.

## Summary for Field Agent Operations
1. **Respect the Handoff**: Only execute what is in the `HANDOFF_MANIFEST`. Do not bleed scope.
2. **Provide Perfect Returns**: Your outputs dictate the orchestrator's state. Always provide exact diffs, file lists, and clear success/fail statuses.
3. **Understand the "Approve" Barrier**: The orchestrator is the brain, you are the hands. The orchestrator approves the plan, but *you* must implement it and send back the evidence.
