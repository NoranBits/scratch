DOC_ID: 08_RESEARCH_GROUNDING_LAYER

Version: v1.0.0
Layer Type: External Knowledge Governance & Deterministic Grounding
Binding: 00–07 (különösen 01_SECURITY + 03_OUTPUT_SCHEMAS + 05_HANDOFF + 07_TOOLING)
Precedencia:
01_SECURITY_LAYER
00_PROTOCOL_LAYER
05_HANDOFF_PROTOCOL_LAYER
07_TOOLING_ARCH_LAYER
08_RESEARCH_GROUNDING_LAYER
03_OUTPUT_SCHEMAS
02_CONTEXT_ARCH_LAYER

I. PURPOSE

Layer 08 definiálja a külső tudás (web, dokumentáció, API, publikációk) determinisztikus bevonásának szabályrendszerét.

Biztosítja:

Zero-trust external intake (01_SECURITY kompatibilis)

Research-before-execution operationalizálása

Időbeli drift kontroll (TTL)

L3 Evidence-alapú grounding

Ez a réteg:

Nem implementál keresést

Nem hajt végre tool-hívást

Nem írja felül a 03 sémákat

Nem módosít governance kapukat

II. RESEARCH GATE (Operationalization of 01 §3)

A 01_SECURITY “Research-before-Execution Gate” elvét műveleti szintre emeli .

Research Trigger (MUST)

Research kötelező, ha:

Missing Evidence → L3-ban nincs releváns EVID

VERIFY capability → 07 alapján CAP:SEARCH:WEB VERIFY

Drift → TTL lejárt

HIGH risk execution előtt külső specifikáció szükséges

Research Default State

RESEARCH_DEFAULT_OFF

Research csak trigger alapján indulhat.

III. SOURCE TRUST LADDER (Normative Mapping)
Tier 1 – Official / Primary

Hivatalos dokumentáció

RFC

Maintainer release note

Default: VERIFY
FACT csak:

verzió explicit

dátum ismert

reprodukálható

L3 injection megtörtént

Tier 2 – Professional Secondary

Szakmai blog

Konferencia anyag

Max TRUST: VERIFY
FACT csak cross-validation esetén.

Tier 3 – Community

StackOverflow

Fórum

Max TRUST: VERIFY
FACT promotion TILOS.

Tier 4 – Unknown / Aggregator

TRUST_LEVEL: UNTRUSTED_DATA

IV. TRUST & EVIDENCE ALIGNMENT (03 Compatible)

Research output nem számít tudásnak, amíg:

Be nem kerül L3 Evidence Registry-be

TRUST_LEVEL nincs meghatározva

STATUS nincs ACTIVE-ra állítva

FACT RULE:
FACT kizárólag:

validated_by = field_agent

validation_method megadva

L3-be injektálva

V. RESEARCH OUTPUT FORMAT (MD_FIRST_ONLY)

Nem új governance card.
Nem új evidence schema.
Külön artefakt, ami L3-ba injektálható.

Repo path ajánlott:
/.ai/EVIDENCE/research_reports/

Minimális mezők:

report_id

trigger_type

executed_by

captured_utc

ttl_policy

source_tier

structured_summary

proposed_evid_id

VI. FRESHNESS / TTL CONTROL

Minden research artefakt tartalmaz:

captured_utc

requires_revalidation_after

TTL ajánlott baseline:

API / Version → 30 nap
Security Advisory → 7 nap
Conceptual → 180 nap

TTL lejárat → DRIFT_TRIGGER (05 integráció).

VII. INTEGRATION WITH 05 & 07

Ha research szükséges:

05_HANDOFF_MANIFEST:

handoff_type: RESEARCH

required_capabilities: CAP:SEARCH:WEB

capability_status: FACT/VERIFY (Adapter Card alapján)

expected_outputs: research_report + new EVID_ID

Return nélkül Anchor nem frissíthető (04 szabály) .

VIII. INTEGRITY & BOUNDARY RULES

NO FACT WITHOUT EVIDENCE
NO SEARCH WITHOUT TRIGGER
NO SOURCE WITHOUT TIER
NO TTL WITHOUT DOMAIN
NO CHAT-ONLY GROUNDING

Precedencia enforcement:
Ha 08 konfliktusba kerül 01_SECURITY-vel → 01 nyer.
Ha 08 konfliktusba kerül 00_PROTOCOL-lal → 00 nyer.