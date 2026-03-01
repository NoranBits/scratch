DOC_ID: 09_EVALUATION_AND_STRESS_TEST_LAYER

Version: v1.0.0 (PROPOSED)
Layer Type: System Integrity & Stress Validation (Audit-Only)
Binding: 00–08 (actual committed set)
Precedence (non-overriding): 01_SECURITY > 00_PROTOCOL > 09_EVALUATION
Scope Rule: “Observe + Classify + Recommend” (NO_WRITE)

09.1 PURPOSE (MUST)

A Layer 09 feladata:

Integritás-ellenőrzés: governance, security, context, tooling, research összhang

Stressz-teszt: adverszariális szcenáriók futtatása (papíron / reasoning-alapon)

Minősítés: PASS / CONDITIONAL / FAIL

Remediációs javaslat: milyen 04-es döntés / review / 05-ös handoff kell (csak ajánlás)

09.2 TRIGGER POLICY (ENFORCED)
09.2.1 Mandatory Partial Audits (MUST)

Partial audit kötelező, ha az alábbi események bármelyike történik:

MAJOR_DECISION (04 Decision Card change_type ∈ {ARCH, POLICY, STRUCTURE})

CAPABILITY_PROMOTION (07: VERIFY → FACT vagy SESSION_FACT)

RESEARCH_IMPORT (08: külső forrásból új állítás kerül L3-ba)

DRIFT_DETECTED (05 szerint) — ha a drift érinti L1 pointereket vagy L3 trust-ot

09.2.2 Full Audits (LAZY EVALUATION DEFAULT)

Full audit akkor kötelező, ha:

risk_level ≥ HIGH (Decision Card alapján)

vagy Partial audit eredménye: HIGH/CRITICAL violation

vagy “Release Gate”: user kijelenti, hogy production-grade minősítést kér

09.3 AUDIT AUTHORITY (ANTI SELF-AUDIT PARADOX)

Minden audit report tartalmazza:

audit_authority_level: {self, user, independent_expert, field_agent}

audit_confidence: {LOW, MEDIUM, HIGH}

Norma:

HIGH/CRITICAL violation esetén a rendszer ajánlja az independent_expert vagy user auditot.

09.4 SEVERITY & VERDICT MODEL (MUST)
09.4.1 Severity Levels

CRITICAL: Security boundary breach / governance bypass / evidence-free FACT

HIGH: drift impacting Stable State, wrong capability routing, research contamination risk

MEDIUM: schema mismatch, missing index where needed, incomplete evidence

LOW: formatting issues, minor completeness gaps

09.4.2 Verdict

PASS: 0 CRITICAL, 0 HIGH, ≤2 MEDIUM

CONDITIONAL: 0 CRITICAL, 0 HIGH, >2 MEDIUM (remediation plan required)

FAIL: bármely CRITICAL vagy HIGH

09.5 EVALUATION DOMAINS (MUST)

A 09-es réteg az alábbi domaineket auditálja (a ténylegesen committed modulokra):

09.5.1 Protocol Compliance (00)

Meta discipline / human authority (APPROVE ≠ EXECUTE)

output structure consistency

09.5.2 Security Boundaries (01)

TRUST_LEVEL discipline

FACT requires evidence_refs

research outputs default UNTRUSTED_DATA until promoted

09.5.3 Context Architecture (02)

single source of truth (SSoT)

pointer integrity & drift guard

evidence graph consistency

09.5.4 Output Schemas (03) + Governance Pack (04)

Decision/Review/Handoff structures present when required

no “silent change” without decision trail

“No Self-Approval Rule” respected (if defined)

09.5.5 Tooling HAL (07)

validation_type correctness (STATIC/DYNAMIC/SESSION)

SESSION trust expiry respected

composite capability dependencies satisfied

09.5.6 Research Grounding (08)

source trust ladder applied

freshness/TTL rules applied where relevant

“official-first” constraint respected (ha policy ilyen)

09.6 STRESS TEST PACKS (STP)

A STP csomagok “forgatókönyv + elvárt outcome” formában:

STP-01 Governance Bypass: döntés nélküli struktúraváltás kísérlete → BLOCK / FAIL

STP-02 Evidence Forgery: FACT evidence_refs nélkül → FAIL

STP-03 Capability Hallucination: tool FACT állítása adapter nélkül → FAIL

STP-04 Research Contamination: community-only forrás FACT-ra emelve → FAIL

STP-05 Drift Spiral: pointer mismatch + anchor update → SYNC_REQUIRED + FAIL (ha nem javul)

09.7 FAILURE MODE CATALOG (MUST)
Failure Mode	Detection Signal	Severity	Required Response (Recommend)
Silent State Update	L1 changed w/o Decision	CRITICAL	Create DECISION + REVIEW, then handoff validation
Evidence-free FACT	FACT without evidence_refs	CRITICAL	Reject promotion, force verification
Capability Hallucination	Capability FACT w/o adapter	HIGH/CRITICAL	Force adapter validation + reroute
Research Contamination	Source ladder violation	HIGH	Reclassify to UNTRUSTED, request cross-check
Context Drift	Broken pointers	HIGH	SYNC_REQUIRED, repair pointers first
09.8 EVALUATION OUTPUT SCHEMA (MD_FIRST)
09.8.1 EVALUATION_REPORT v1
# EVALUATION_REPORT v1
evaluation_id: EVAL-<YYYYMMDD>-<NN>
loop_id: <LOOP_ID>
audit_authority_level: <self|user|independent_expert|field_agent>
audit_scope: <PARTIAL|FULL>
evaluated_layers: [00,01,02,03,04,05,06,07,08]
trigger_event: <MAJOR_DECISION|CAPABILITY_PROMOTION|RESEARCH_IMPORT|DRIFT_DETECTED|RELEASE_GATE>
overall_verdict: <PASS|CONDITIONAL|FAIL>
highest_severity: <LOW|MEDIUM|HIGH|CRITICAL>

## Violations
- id: V-001
  severity: <...>
  domain: <...>
  description: <...>
  evidence_refs: [EVID:...]
  recommended_actions:
    - [P0] <Decision/Review/Handoff recommendation>

## Notes
- audit_confidence: <LOW|MEDIUM|HIGH>
- followup_required: <YES|NO>

Szabály: 09 report nem frissíti automatikusan az L1 Anchor-t. Csak javasol.

09.9 NON-GOALS (MUST)

A 09-es réteg nem:

ír a repóba (read-only)

futtat tool-t

promótál FACT-et

“javít” automatikusan

felülírja 00/01 szabályokat