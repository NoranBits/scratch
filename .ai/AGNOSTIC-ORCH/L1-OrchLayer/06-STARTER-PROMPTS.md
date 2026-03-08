# Starter Prompts

These prompts are designed for everyday use with OrchLayer GPT inside ChatGPT Projects.

---

## 1. General Starter

```text
Act as the L1 Orchestrator defined in the Knowledge files.

Mode: normal
Goal: [insert the current goal]
Scope: [insert what is in scope and what is out of scope]
Required output: [insert the artifact needed]
Constraints: [insert constraints]

Help me structure the task, preserve scope, and move toward the required output.
If continuity becomes important, generate a compact Session Packet at the end.
```

---

## 2. Review / Peer Review Starter

```text
Act as the L1 Orchestrator defined in the Knowledge files.

Mode: review
Goal: Review the following system / document / architecture.
Scope: Focus on goal alignment, scope discipline, role consistency, continuity quality, handoff readiness, drift resistance, and practical usefulness.
Required output: Structured peer review with strengths, weaknesses, risks, and highest-value corrections.
Constraints: Be exact, constructive, and compact.

Input:
[paste the material here]
```

---

## 3. Session Continuity Starter

```text
Act as the L1 Orchestrator defined in the Knowledge files.

Mode: session-refresh
Goal: Restore and continue this work using the session context below.
Required output: Re-anchored continuation plan plus next-step support.
Constraints: Use only the state provided below unless I add more.

Session Packet:
[paste session packet here]
```

---

## 4. Handoff Starter

```text
Act as the L1 Orchestrator defined in the Knowledge files.

Mode: handoff
Goal: Prepare a clean handoff package for the next actor.
Target: [human / reviewer / executor / new-chat / other-ai]
Required output: Structured Handoff Package with constraints, expected artifact, open questions, and bootstrap prompt.
Context:
[paste current state or material here]
```

---

## 5. Project Kickoff Starter

```text
Act as the L1 Orchestrator defined in the Knowledge files.

Mode: review
Goal: Help me initialize this project workspace and define a clean working structure.
Scope: Identify the active goal, boundaries, risks, output needs, and continuity strategy.
Required output:
1. Working interpretation of the project
2. Recommended structure for this workspace
3. Immediate next steps
4. Compact Session Packet
Constraints: Keep it practical and optimized for long-running work inside ChatGPT Projects.

Project context:
[paste project summary here]
```

---

## 6. System Refinement Starter

```text
Review your current operating model as an L1 Orchestrator.

Assess:
- clarity of role
- boundary discipline
- response mode selection
- session continuity behavior
- handoff quality
- drift control
- usability inside ChatGPT Projects

Then propose:
1. weaknesses
2. misalignment risks
3. exact instruction improvements
4. revised wording where needed
```

---

## 7. Daily Use Short Prompt

```text
Act as my L1 Orchestrator.

Goal: [goal]
Scope: [scope]
Needed output: [output]
Constraints: [constraints]

Keep the answer compact and structured only as needed.
Generate a Session Packet only if continuity matters.
```
