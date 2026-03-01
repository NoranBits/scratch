KB DOC_ID: 03_OUTPUT_SCHEMAS (v1.0.1 FINAL – MD_FIRST / READ-ONLY ALIGNED)
0. SCOPE & PRECEDENCE (NORMATIVE)
Scope: Markdown-first sablonok az L1–L3 kontextus artefaktokhoz (02_CONTEXT_ARCH_LAYER szerinti helyeken), kifejezetten In-App Orchestrator (Read-Only) működéshez.
Precedence: 01_SECURITY > 00_PROTOCOL > 03_OUTPUT_SCHEMAS > 02_CONTEXT_ARCH.
No Override: A 03-as sémák semmilyen körülmények között nem írhatják felül a 00/01 szabályokat.
1. GLOBAL CONVENTIONS (ENFORCED)
Megjegyzés: [ROOT] a 06_WORKPLACE_LAYOUT_LAYER ROOT_POLICY szerint `/.ai/` vagy `/ai/` (fallback) gyökér.
1.1 Authority Separation (MUST)
Orchestrator = proposed_by (csak javaslat, instrukció, prompt, audit)
Field Agent / User = executed_by (repo-művelet, validáció, “tényesítés”)
APPROVE ≠ EXECUTE: jóváhagyás sem jelent automatikus repo-változtatást.
1.2 Trust & Status Policy (MUST)
TRUST_LEVEL ∈ {FACT, VERIFY, UNTRUSTED_DATA}
STATUS ∈ {ACTIVE, SUPERSEDED, DEPRECATED}
FACT RULE (MUST): TRUST_LEVEL=FACT csak akkor megengedett, ha validated_by=field_agent és validation_method meg van adva.
1.3 Evidence ID Convention (MUST)
EVID_ID formátum: EVID:<TYPE>:<YYYYMMDD>:<NNNN>
TYPE ajánlott értékek: DOC | CODE | DIFF | TEST | LINK | NOTE
Példa: EVID:TEST:20260223:0007
1.4 Read-Only Execution Status (MUST)
Minden L1/L2/L3 dokumentum tartalmazza:
execution_status ∈ {DRAFT, PENDING_AGENT_WRITE, IN_REPO, VERIFIED}
executed_by ∈ {field_agent, user}
1.5 Minimalism Rule (SHOULD)
A sémák “minimum viable” mezőket használnak; bővítés (hash, artifact digests, stb.) csak későbbi rétegben (pl. 07) történjen.
2. SCHEMA L1 – STABLE_STATE_ANCHOR (Level 1)
Repo path (02 szerint): [ROOT]/STATE/stable_state.md
Cél: az Orchestrator által értelmezhető, rövid “igazság-snapshot” a jelenlegi célról, döntési állapotról és drift pointerekről.
Tiltás: nyers evidenciák részletezése itt TILOS (az L3 dolga).
Markdown
Kód másolása
# STABLE_STATE_ANCHOR (L1) v1.0.1
schema_id: 03_SCHEMA_L1_STABLE_STATE_ANCHOR
loop_id: <LOOP_ID>
proposed_by: <orchestrator_id>
executed_by: <field_agent|user>
execution_status: <DRAFT|PENDING_AGENT_WRITE|IN_REPO|VERIFIED>
last_updated_utc: <YYYY-MM-DDTHH:MM:SSZ>

## Current Objective (MUST)
- objective: <1-2 mondat, mérhető cél>

## Decision Snapshot (MUST)
- last_committed_id: <KB_* vagy DECISION_CARD id>
- pending_decisions:
  - <D1 röviden>
  - <D2 röviden>

## Feature Flags (MUST)
- STATE_DISCIPLINE: ACTIVE
- COUNCIL_MODE: OFF
- LOG_DELIBERATION: OFF

## Drift Guard Pointers (MUST)
- active_task_path: [ROOT]/TASKS/active_task.md
- evidence_registry_path: [ROOT]/EVIDENCE/registry.md
- loops_path: [ROOT]/LOOPS/loop_counter.md

## Notes (SHOULD)
- <max 5 bullet, nincs hosszú narratíva>
3. SCHEMA L2 – ACTIVE_TASK (Level 2)
Repo path (02 szerint): [ROOT]/TASKS/active_task.md
Cél: “mit csinálunk most” – scope + DoD + prioritásos next actions.
MUST: DoD mérhető és validációs módszerrel megadott.
Markdown:
# ACTIVE_TASK (L2) v1.0.1
schema_id: 03_SCHEMA_L2_ACTIVE_TASK
loop_id: <LOOP_ID>
instruction_source: <orchestrator_id>
field_agent_assigned: <agent_id|user>
execution_status: <DRAFT|PENDING_AGENT_WRITE|IN_REPO|VERIFIED>
last_updated_utc: <YYYY-MM-DDTHH:MM:SSZ>

## Scope (MUST)
- in_scope:
  - <max 7 bullet>
- out_of_scope:
  - <max 7 bullet>

## Definition of Done (MUST)
- [ ] <kritérium 1> | validation_method: <test|diff|doc|repro> | evidence_expected: <EVID:...>
- [ ] <kritérium 2> | validation_method: <test|diff|doc|repro> | evidence_expected: <EVID:...>

## Next Actions (MUST, P0-P2)
- [P0] <konkrét, végrehajtható lépés>
- [P0] <konkrét, végrehajtható lépés>
- [P1] <opcionális>
- [P2] <opcionális>

## Blockers / Questions (SHOULD)
- <max 5 bullet>
4. SCHEMA L3 – EVIDENCE_REGISTRY (Level 3)
Repo path (02 szerint): [ROOT]/EVIDENCE/registry.md
Cél: a “valóság hídja” az Orchestrator felé: minden fontos állítás egy EVID_ID-re mutat.
MUST: TRUST_LEVEL + STATUS + rövid summary.
FACT RULE: FACT csak field_agent validációval.
Markdown:
# EVIDENCE_REGISTRY (L3) v1.0.1
schema_id: 03_SCHEMA_L3_EVIDENCE_REGISTRY
verification_authority: field_agent_only
last_updated_utc: <YYYY-MM-DDTHH:MM:SSZ>

| EVID_ID | TYPE | SOURCE | TRUST_LEVEL | STATUS | validated_by | validation_method | SUMMARY |
|---|---|---|---|---|---|---|---|
| EVID:DOC:20260223:0001 | DOC | [ROOT]/docs/spec.md | VERIFY | ACTIVE | field_agent | doc_review | Rövid összefoglaló |
| EVID:TEST:20260223:0002 | TEST | tests/report.txt | FACT | ACTIVE | field_agent | test | Teszt igazolja X-et |
| EVID:CODE:20260223:0003 | CODE | src/main.py | VERIFY | ACTIVE | field_agent | diff | Változás javasolt |
Kötelező ellenőrzések (MUST):
Ha TRUST_LEVEL=FACT → validated_by=field_agent és validation_method NEM üres.
Ha egy elem elavult → STATUS=SUPERSEDED és az új EVID_ID szerepeljen a SUMMARY-ban (“Superseded by …”).
5. INTEGRITY RULES (ENFORCED)
5.1 No Duplicate Truth (MUST)
L1 nem tartalmazhat evidenciát; L3 a tények regisztere.
L2 nem “napló”, hanem végrehajtási keret.
5.2 Drift Guard (MUST)
L1 pointerek kötelezőek; ha hiányoznak → Orchestrator Step 7-ben CLARIFY.
5.3 Minimal Required Fields (MUST)
A fenti kötelező mezők hiánya esetén a dokumentum nem tekinthető VERIFIED-nek.