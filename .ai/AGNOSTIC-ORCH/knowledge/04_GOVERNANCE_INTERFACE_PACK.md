DOC_ID: 04_GOVERNANCE_INTERFACE_PACK
Version: v1.1.0 FINAL
Layer Type: Governance Gate & Structured Execution Interface
Binding: MASTER_SYSTEM_INSTRUCTION_AI_AGNOSTIC_v1.2_EXTENSIVE
I. PURPOSE
Layer 04 formalizálja a Multi-Expert In-App Orchestrator governance mechanizmusát.
Ez a réteg biztosítja:
Strukturált döntési kapuk
Auditálható szakmai kritika
Capability-aware handoff interfész
Kontrollált self-improvement ciklus
Drift-minimalizáló governance trace
Ez a réteg:
Nem módosítja a 00_PROTOCOL_LAYER szabályait
Nem írja felül a 01_SECURITY_LAYER enforcement mechanizmusait
Nem érinti a 02_CONTEXT_ARCH determinisztikus load order-t
Nem módosítja a 03_OUTPUT_SCHEMAS sémáit
Precedencia:
01_SECURITY
00_PROTOCOL
04_GOVERNANCE
03_OUTPUT_SCHEMAS
02_CONTEXT_ARCH
II. GOVERNANCE FOUNDATIONS (NORMATIVE)
DECISION IS REQUIRED FOR STRUCTURAL CHANGE
Minden architekturális, policy, workflow vagy repo-strukturális változtatás DECISION_CARD-on keresztül történik.
REVIEW IS REQUIRED FOR LEGITIMACY
Jelentős változtatás csak REVIEW_CARD validáció után tekinthető governance-legitimnek.
SELF-IMPROVEMENT CONSTRAINT
A rendszer önjavítása kizárólag:
Valid Evidence (L3)
REVIEW_CARD kombinációján keresztül történhet.
APPROVE STRICTNESS
Strict APPROVE tokens are only required for high-level decisions affecting project behavior. Routine in-app executions within the repository can auto-proceed once the orchestrator issues a valid HANDOFF_MANIFEST.
TRACEABILITY MANDATE
Minden governance artefakt kötelezően tartalmaz:
loop_id
hivatkozást L1/L2/L3 elemekre
NO CHAT-ONLY GOVERNANCE
Chatben elhangzott döntés nem tekinthető érvényesnek DECISION_CARD nélkül.
III. DECISION_CARD SPECIFICATION
Repo ajánlott path:
[ROOT]/GOVERNANCE/decisions/<decision_id>.md
DECISION_CARD v1.1.0
schema_id: 04_SCHEMA_DECISION_CARD
decision_id: DEC--
loop_id: <LOOP_ID>
proposed_by: <orchestrator_id>
authority: <user | council_consensus>
created_utc: YYYY-MM-DDTHH:MM:SSZ
1. Decision Classification (MUST)
change_type: <ARCH | REFACTOR | FEATURE | POLICY | STRUCTURE | SECURITY>
scope_type: <LOCAL | CROSS_LAYER | SYSTEMIC>
urgency: <LOW | NORMAL | HIGH | CRITICAL>
2. Objective & Rationale (MUST)
objective: <mérhető cél>
rationale: <miért szükséges, milyen problémát old>
3. Constitutional & Security Check (MUST)
conflicts_with_00_PROTOCOL: <true|false>
conflicts_with_01_SECURITY: <true|false>
requires_security_review: <true|false>
requires_independent_review: <true|false>
Ha bármely true → REVIEW_CARD kötelező.
4. Impact & Risk Analysis (MUST)
affected_layers:
<00|01|02|03|04|repo>
risk_level: <LOW | MEDIUM | HIGH>
failure_mode_description: 
rollback_strategy: <konkrét lépések>
5. Evidence Base (L3 Reference)
supporting_evidence:
EVID:...
pending_verification:
EVID:...
FACT nélküli döntés csak feltételes.
6. Approval Block
review_status: <NOT_REQUIRED | PENDING | COMPLETED>
final_status: <PENDING | APPROVED | REJECTED>
approved_by: <user | council>
approved_utc: YYYY-MM-DDTHH:MM:SSZ
IV. REVIEW_CARD SPECIFICATION
Repo ajánlott path:
[ROOT]/GOVERNANCE/reviews/<review_id>.md
REVIEW_CARD v1.1.0
schema_id: 04_SCHEMA_REVIEW_CARD
review_id: REV--
loop_id: <LOOP_ID>
target_id: <DEC-XXXX | TASK-XXXX | DOC-XXXX>
reviewed_by: <role_or_entity>
created_utc: YYYY-MM-DDTHH:MM:SSZ
1. Reviewer Independence (MUST)
reviewer_role: <independent | same_author>
independence_verified: <true|false>
Ha same_author → verdict nem lehet APPROVE.
2. Structured Evaluation (MUST)
Strengths
<min 2 bullet>
Weaknesses
<min 2 bullet>
Identified Risks
<min 2 bullet>
3. Evidence Alignment (MUST)
validated_evidence:
EVID:...
disputed_or_missing_evidence:
EVID:...
FACT státusz csak L3 alapján.
4. Verdict & Enforcement
verdict: <APPROVE | REVISE | REJECT>
enforcement_required: <true|false>
required_actions:
[P0] <kötelező módosítás>
[P1] <ajánlott módosítás>
V. HANDOFF_MANIFEST SPECIFICATION
Repo ajánlott path:
[ROOT]/HANDOFFS/<handoff_id>.md
HANDOFF_MANIFEST v1.1.0
schema_id: 04_SCHEMA_HANDOFF_MANIFEST
handoff_id: HOFF--
loop_id: <LOOP_ID>
platform_self: <orchestrator_id>
target_platform: <agent_id | user>
created_utc: YYYY-MM-DDTHH:MM:SSZ
1. Identity & Intent (MUST)
handoff_type: <EXECUTION | RESEARCH | VALIDATION>
reasoning: <miért szükséges>
risk_level: <LOW | MEDIUM | HIGH>
2. Capability Contract (MUST)
required_tools:
<tool_name>
capability_status: <FACT | VERIFY>
capability_checked_against_adapter_card: <true|false>
fallback_strategy_if_unavailable: <leírás>
FACT csak Adapter Card alapján.
3. Execution Packet (MUST)
related_decision_id: DEC-XXXX
related_task_path: [ROOT]/TASKS/active_task.md
related_evidence_ids:
EVID:...
expected_outputs:
file_modifications
evidence_updates
validation_artifacts
4. Mandatory Return Contract (MUST)
updated_files:

updated_evidence_ids:
EVID:...
validation_method_used:
<test | diff | doc | repro>
unresolved_items:

execution_summary:
<max 10 sor>
Hiányos return → Anchor nem frissíthető.
VI. GOVERNANCE INTEGRITY RULES (ENFORCED)
NO DECISION WITHOUT TRACE
loop_id hiánya → invalid document.
NO REVIEW WITHOUT EVIDENCE
Evidence reference nélkül review nem valid.
NO HANDOFF WITHOUT CAPABILITY CHECK
Capability mezők hiánya → invalid manifest.
PRECEDENCE ENFORCEMENT
01_SECURITY mindig felülírja 04-et.
00_PROTOCOL mindig felülírja 04-et.
NO SILENT STATE TRANSITION
Governance artefakt nélkül Anchor nem frissülhet.
VII. SCOPE BOUNDARY
Layer 04 nem tartalmaz:
Trigger döntési fát
Routing algoritmust
Tool adapter implementációt
Research search policy-t
Ezek külön rétegek:
05_HANDOFF_PROTOCOL_LAYER
06_WORKPLACE_LAYOUT_LAYER
07_TOOLING_ARCH_LAYER
08_RESEARCH_GROUNDING_LAYER
VIII. STATUS
04_GOVERNANCE_INTERFACE_PACK v1.1.0 FINAL
Header-safe
Kernel-aligned
Security-compliant
Read-Only Orchestrator kompatibilis
Deterministic governance ready