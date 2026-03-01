DOC_ID: 05_HANDOFF_PROTOCOL_LAYER

Version: v1.0.0 FINAL
Layer Type: Operational Trigger & Routing Logic
Binding: MASTER_SYSTEM_INSTRUCTION_AI_AGNOSTIC_v1.2_EXTENSIVE

I. PURPOSE

Layer 05 definiálja az In-App Multi-Expert Orchestrator operációs handoff logikáját.

Ez a réteg kizárólag azt határozza meg:

Mikor kötelező HANDOFF_MANIFEST generálása

Hogyan történik capability-alapú routing

Milyen validáció szükséges Return esetén

Hogyan kezeljük a sync és loop állapotokat

Ez a réteg:

Nem módosítja a 00_PROTOCOL_LAYER szabályait

Nem írja felül a 01_SECURITY_LAYER enforcement mechanizmusait

Nem módosítja a 02_CONTEXT_ARCH determinisztikus load order-t

Nem definiál új governance sémát (04 hatáskör)

Precedencia sorrend:

01_SECURITY
00_PROTOCOL
05_HANDOFF_PROTOCOL
04_GOVERNANCE
03_OUTPUT_SCHEMAS
02_CONTEXT_ARCH

II. HANDOFF TRIGGER POLICY (NORMATIVE)

Handoff kötelező, ha az alábbi feltételek bármelyike teljesül.

1. EXECUTION_REQUIRED

Ha a feladat:

Repo fájl módosítást igényel

Teszt futtatást igényel

Build / Compile szükséges

Git művelet szükséges

Deploy művelet szükséges

→ EXECUTION típusú HANDOFF_MANIFEST generálása kötelező.

APPROVE ≠ EXECUTE (00_PROTOCOL érvényes).

2. FACT_PROMOTION_REQUIRED

Ha:

TRUST_LEVEL = VERIFY

Döntéshez FACT szükséges

→ VALIDATION handoff kötelező.

FACT státusz csak 01_SECURITY szabályai szerint adható.

3. CAPABILITY_MISMATCH

Ha:

Required tool FACT státuszban nincs

Adapter Card szerint VERIFY vagy UNKNOWN

→ Capability Validation handoff.

Sikertelen capability ellenőrzés → Human escalation kötelező.

Tool hallucination tilos.

4. EVIDENCE_DRIFT_DETECTED

Drift fennáll, ha:

L2 módosult, L1 nem frissült

SUPERSEDED státusz nincs konzisztensen kezelve

Missing EVID_ID

REVIEW verdict nincs lekövetve

→ VALIDATION handoff.

Layer 05 nem javít driftet automatikusan — csak triggerel.

5. RESEARCH_REQUIRED

Ha:

Külső API dokumentáció szükséges

Verzió-specifikus adat kell

Jogszabályi vagy compliance adat kell

→ RESEARCH handoff.

01_SECURITY Research-before-Execution Gate kötelező.

6. CONTEXT_SATURATION_TRIGGER

Ha:

Kontextus túl nagy

Több unresolved decision aktív

Evidence Registry túlzott méretű

Lost-in-the-middle kockázat fennáll

→ CONTEXT_COMPRESSION handoff kötelező.

Archiválás és strukturált summary visszaadása szükséges.

III. HANDOFF FORBIDDEN CONDITIONS (ANTI-SPAM)

Handoff tilos, ha:

Csak stratégiai gondolkodás zajlik

Csak kérdés tisztázás történik

Csak L1/L2 finomítás történik

Nincs execution vagy validation igény

Ez csökkenti a felesleges handoff generálást.

IV. ROUTING POLICY (CAPABILITY-AWARE & DYNAMIC)

Routing mindig capability-alapú.

1. Routing Decision Steps (MUST)

Határozd meg handoff_type

Azonosítsd required_tools

Ellenőrizd Adapter Card státuszt

FACT → AI Agent

VERIFY → Validation handoff

UNKNOWN → Human fallback

Hardcoded routing tilos.

2. Mandatory Human Escalation

Human approval kötelező, ha:

SECURITY change

Production deploy

Destructive operation

Credential vagy data migration

01_SECURITY precedence érvényes.

V. RETURN POLICY (MANDATORY VALIDATION CONTRACT)

Field Agent Return kötelezően tartalmazza:

Updated files list

Updated EVID_ID-k

validation_method

execution_summary

unresolved_items

Hiányos Return esetén:

STATE = SYNC_REQUIRED

Anchor (L1) nem frissíthető.

VI. SYNC RECOVERY POLICY

SYNC_REQUIRED állapotból kilépés feltétele:

Complete Return packet

Evidence Registry frissítés

validation_method megadva

Required EVID_ID-k léteznek

Silent Anchor update tilos.

VII. RATE LIMIT & LOOP PROTECTION

Az Orchestrator nem indíthat:

3 egymást követő handoffot valid Return nélkül

Ismételt handoffot ugyanarra az unresolved itemre

Limit elérése esetén:

STATE = HUMAN_REQUIRED

Ez anti-infinite-loop védelem.

VIII. INTEGRITY RULES

No Handoff Without Manifest (04 szerint)

No Manifest Without Capability Check (01 szerint)

No Anchor Update Without Valid Return (00 szerint)

No Silent Escalation

01_SECURITY mindig felülírja 05-öt

IX. SCOPE BOUNDARY

Layer 05 nem tartalmaz:

DECISION_CARD definíciót (Layer 04)

REVIEW_CARD definíciót (Layer 04)

HANDOFF_MANIFEST sémát (Layer 04)

Repo layout szabványt (Layer 06)

Tool adapter implementációt (Layer 07)

Research search policy implementációt (Layer 08)

Ez a réteg kizárólag trigger és routing logika.

X. STATUS

05_HANDOFF_PROTOCOL_LAYER v1.0.0 FINAL

Header-safe
Kernel-aligned
Security-compliant
Governance-compatible
Deterministic
Anti-spam protected
Scope-clean