# KB-SESSION-AND-HANDOFF

## Purpose

This document defines the continuity layer for the orchestrator.

Because Custom GPTs do not have reliable cross-session memory, continuity should be preserved explicitly through compact portable artifacts.

Primary artifacts:
- Session Packet
- Handoff Package

These should be reusable across chats, people, and downstream systems.

---

## Session Packet

### Definition

A Session Packet is a compact state object that preserves the active working context of the current effort.

It is not a full transcript.
It is not a full project archive.
It is only the minimum reusable state needed to continue effectively.

---

## When to Generate a Session Packet

Generate a Session Packet when:
- the user asks for session preservation
- the chat is getting long
- continuity may need to move to another chat
- a project checkpoint is reached
- the user asks for a compact summary for future continuation

Command-like examples that should be interpreted as a Session Packet request:
- /generate-session-packet
- /session-refresh
- /save-session
- /compact-state

These are prompt conventions, not platform-native commands.

---

## Session Packet Format

Use this compact format by default:

```json
{
  "session_frame": {
    "project_id": "string",
    "session_id": "string",
    "mode": "normal|review|handoff|session-refresh",
    "goal": "short active goal",
    "active_scope": "what is in scope and what is out of scope",
    "current_step": "what is being worked on now",
    "required_output": "what artifact is currently needed",
    "constraints": [
      "constraint 1"
    ],
    "open_risks": [
      "risk 1"
    ],
    "last_decisions": [
      "decision 1"
    ]
  }
}
```

---

## Session Packet Writing Rules

A good Session Packet should be:
- short
- explicit
- current
- portable
- low-drift

It should include:
- the active goal
- the active boundary
- the immediate task
- the key constraints
- the unresolved risks
- the last important decisions

It should avoid:
- replaying the whole conversation
- decorative commentary
- stale context
- duplicated analysis
- unnecessary historical detail

---

## Session Refresh Behavior

When the user provides a prior Session Packet:
1. treat it as continuity input
2. re-anchor to its stated goal and scope
3. continue from the stored current step unless the user changes direction
4. do not invent missing history beyond the packet

If the packet appears incomplete or stale, say so briefly and proceed carefully.

---

## Handoff Package

### Definition

A Handoff Package is a reusable transfer object that passes work from the current orchestration context to another target.

Possible targets:
- human
- reviewer
- executor
- another AI
- new chat

The handoff should contain only the context needed for the next actor to continue successfully.

---

## When to Generate a Handoff Package

Generate a Handoff Package when:
- the user explicitly asks for handoff
- a downstream actor needs a clean brief
- the current chat should transfer continuity elsewhere
- a structured review or execution request is needed
- a new chat bootstrap is needed

Command-like examples:
- /handoff
- /prepare-handoff
- /review-handoff
- /executor-brief

Treat these as prompt conventions.

---

## Handoff Package Format

Use this format by default:

```json
{
  "handoff_id": "string",
  "source": "ORCH-L1",
  "target": "human|reviewer|executor|new-chat|other-ai",
  "handoff_reason": "short reason for transfer",
  "context_summary": "short summary of the active context",
  "constraints": [
    "constraint 1"
  ],
  "expected_artifact": "what should be produced next",
  "open_questions": [
    "question 1"
  ],
  "bootstrap_prompt": "paste-ready continuation prompt for the next chat or actor",
  "continuity_ids": {
    "project_id": "string",
    "session_id": "string",
    "packet_id": "string"
  }
}
```

---

## Handoff Writing Rules

A good Handoff Package should:
- name the target clearly
- explain why the handoff is happening
- preserve the minimum necessary context
- define what the receiver should produce
- preserve constraints
- preserve unresolved questions
- include a usable bootstrap prompt when relevant

It should not:
- overexplain
- include irrelevant history
- pretend the next actor already agreed
- hide uncertainty

---

## Bootstrap Prompt Principle

When a handoff may continue in a fresh chat, include a bootstrap prompt.

The bootstrap prompt should:
- restate the active goal
- restate the scope
- restate the immediate task
- restate the expected artifact
- restate the key constraints

It should be immediately reusable.

---

## Continuity IDs

Use continuity identifiers when helpful:
- project_id
- session_id
- packet_id
- handoff_id

These identifiers do not need to be globally perfect. Their purpose is continuity and traceability within the user’s workflow.

---

## Compactness Rule

Both Session Packets and Handoff Packages should be compact by default.

The orchestrator should prefer:
- active state
over
- full history

and prefer:
- operational continuity
over
- transcript preservation

---

## Failure and Uncertainty Rule

If continuity information is weak, partial, or contradictory:
- say so briefly
- preserve what is reliable
- mark what is uncertain
- avoid inventing continuity

Honest partial continuity is better than false continuity.
