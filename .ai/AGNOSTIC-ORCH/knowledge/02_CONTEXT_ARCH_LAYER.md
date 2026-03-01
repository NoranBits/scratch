DOC_ID: 02_CONTEXT_ARCH_LAYER
Version: v2.1.0 FINAL
Layer Type: In-App Deterministic Context Architecture
Binding: MASTER_SYSTEM_INSTRUCTION_AI_AGNOSTIC_v1.2_EXTENSIVE
I. PURPOSE
Layer 02 definiálja az In-App Multi-Expert Orchestrator determinisztikus kontextusarchitektúráját.
Cél:
Hierarchikus kontextuskezelés
Drift minimalizálás
Strukturált Evidence memória
RAG-optimalizált tudásaktiválás
Token-hatékony működés
Ez a réteg nem enforcement réteg, hanem strukturális kontextus-architektúra.
II. DETERMINISTIC CONTEXT LOAD ORDER (LEVELS 0–4)
A kontextus betöltése fix sorrendben történik.
LEVEL 0 — Canon (Immutable Governance Layer)
Tartalom:
MASTER_SYSTEM_INSTRUCTION_AI_AGNOSTIC_v1.2_EXTENSIVE
00_PROTOCOL_LAYER
01_SECURITY_LAYER
Tulajdonság:
Nem felülírható
Minden más réteg felett áll
SECURITY > CORE > CONTEXT precedencia érvényes
LEVEL 1 — Stable State Anchor
Az aktuális működési igazságforrás.
Minimum mezők:
current_objective
current_loop_id
decision_snapshot
active_constraints
Szabály:
Csak explicit APPROVE után frissíthető
Nem implicit
Nem generálható csendben
LEVEL 2 — Active Task Context
Operatív fókusz réteg.
Tartalom:
Scope
Non-goals
Definition of Done
Dependencies
Risks
Nem tartalmaz történeti zajt.
LEVEL 3 — Evidence Graph
Strukturált tudásmemória.
Schema:
| EVID_ID | CATEGORY | TRUST_LEVEL | STATUS | RELEVANCE | SUMMARY |
CATEGORY:
CODE
DESIGN
ARCH
DOC
TEST
USER_INPUT
DECISION
TRUST_LEVEL:
FACT
VERIFY
UNTRUSTED_DATA
STATUS:
ACTIVE
SUPERSEDED
DEPRECATED
RELEVANCE:
HIGH
MEDIUM
LOW
Fontos:
Az Evidence Graph támogatja a drift-észlelést,
de nem automatizált enforcement mechanizmus.
LEVEL 4 — Historical Context
Tartalom:
Korábbi Anchor snapshotok
Archív döntések
Loop státusz
Csak audit vagy konfliktus esetén aktiválódik.
III. RAG-OPTIMIZED STRUCTURAL GUIDELINES
Ez strukturális optimalizáció, nem governance enforcement.
Alapelvek:
Rövid, strukturált Anchor
Szelektív Evidence aktiválás (HIGH + ACTIVE default)
History csak szükség esetén
Deep Structure Guideline
Sub-INDEX vagy al-strukturálás javasolt, ha:
12+ fájl
3+ al-mappa
Ez teljesítmény-optimalizációs ajánlás,
nem protokoll-szintű kötelezettség.
IV. DRIFT CONTROL PRINCIPLES
Drift akkor történhet, ha:
Anchor elavul
Evidence státusz nincs frissítve
Task változik Anchor frissítés nélkül
Mitigáció:
STATUS mező kötelező
SUPERSEDED nem aktiválható
Anchor frissítés explicit
V. KERNEL PRECEDENCE CLARIFICATION (CRITICAL)
Layer 02:
Nem írhatja felül a 00_PROTOCOL_LAYER szabályait
Nem írhatja felül a 01_SECURITY_LAYER korlátait
Nem módosíthatja a precedencia sorrendet
Amennyiben konfliktus merül fel:
👉 01_SECURITY_LAYER
👉 00_PROTOCOL_LAYER
mindig elsőbbséget élvez a 02_CONTEXT_ARCH_LAYER-rel szemben.
Strukturális optimalizáció nem írhatja felül governance enforcement-et.
VI. SCOPE BOUNDARY
Layer 02 nem tartalmaz:
Handoff protokollt
Debate engine logikát
Multi-platform runtime koordinációt
Tooling capability deklarációt
Ezek külön KB rétegek.