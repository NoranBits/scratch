DOC_ID: 07_TOOLING_ARCH_LAYER
Version: v1.0.1 FINAL
Layer Type: Operational HAL / Capability Abstraction
Binding: 00–06 (különösen 02 Security + 05 Handoff + 06 Layout)
Precedencia: 01_SECURITY_LAYER > 00_PROTOCOL_LAYER > 05_HANDOFF_PROTOCOL_LAYER > 07_TOOLING_ARCH_LAYER
Normatív Scope: a 07 képességeket definiál + platform-mappinget; nem ír elő konkrét tool-parancsokat.
4.1 Cél és definíciók (MUST)
Capability (CAP): stabil azonosító + intent + kockázat + validációs elvárás.
Adapter Card: platform-specifikus elérhetőség és bizalom (FACT/VERIFY), evidence-hivatkozásokkal.
Registry: derivált összegzés routinghoz; SSoT az Adapter Card.
Session-level FACT: csak validation_type=SESSION és risk=LOW esetén; session végén automatikus visszaesés VERIFY-re.
4.2 Kötelező fájl-elhelyezés (06-tal kompatibilis)
Primary root: /.ai/
Fallback root: /ai/ (csak ha szükséges; DUAL ROOT TILOS)
Ajánlott:
/.ai/TOOLING/capability_model.md
/.ai/TOOLING/platform_adapter_cards.md
/.ai/TOOLING/capability_registry.md
/.ai/TOOLING/INDEX.md (INDEX_IF_EXISTS szabállyal)
4.3 Capability Model (MD_FIRST) – normatív mezők
MUST mezők minden CAP definícióban:
capability_id (pl. CAP:REPO:READ_TREE)
intent
risk: LOW|MEDIUM|HIGH
validation_type: STATIC|DYNAMIC|SESSION
dependencies: [CAP:...] (Composite esetén nem üres)
transient_failure_policy:
on_failure: RETRY_THEN_VERIFY|VERIFY_AND_ROUTE|STOP_AND_ESCALATE
retry_budget: szám (min 0)
fallback: HUMAN_REQUIRED_IF_BLOCKING|HUMAN_REQUIRED|ROUTE_TO_AGENT
required_returns (MEDIUM/HIGH esetén MUST)
forbidden_claims (anti-hallucination)
Példa (rövid):
Markdown:
- capability_id: CAP:REPO:READ_TREE
  intent: List files/directories in repo
  risk: LOW
  validation_type: SESSION
  dependencies: []
  transient_failure_policy: { on_failure: RETRY_THEN_VERIFY, retry_budget: 1, fallback: HUMAN_REQUIRED_IF_BLOCKING }
  required_returns: [ { evidence: EVID:LISTING:..., trust_promotion: VERIFY->FACT } ]
  forbidden_claims: [ "Assume repo access without adapter FACT" ]
4.4 Composite Capabilities (MUST)
Composite CAP csak dependencies-t deklarál.
Composite CAP nem emel TRUST_LEVEL-t önmagában; a komponensek evidence-e dönt.
Példa:
CAP:CODE:REFACTOR dependencies: CAP:REPO:READ_FILE, CAP:REPO:APPLY_PATCH, CAP:TEST:RUN
4.5 Platform Adapter Card (MD_FIRST) – normatív
Kötelező oszlopok: capability_id | availability | confidence | validation_type | notes | validation_method | last_validated_utc | evidence_refs
Szabályok (MUST):
confidence=FACT → evidence_refs nem lehet üres (vagy explicit “human assertion” + REVIEW kötelező).
validation_type adapter oldalon egyezzen a capability modellel; eltérés = DRIFT.
availability=UNKNOWN vagy confidence=VERIFY → 05_HANDOFF “VALIDATION” handoff kötelező, ha blocking.
4.6 Capability Registry (derivált, routing-barát)
A registry csak összegzés; konfliktus esetén az Adapter Card a valóság.
4.7 Validation Types – pontos jelentés
STATIC: ritkán változó; FACT tartható amíg “stale” trigger nem jelzi.
DYNAMIC: minden használatkor validálandó (pl. web elérés); default VERIFY.
SESSION: csak LOW risk read; FACT “gyorsítótár” session végéig.
4.8 Baseline készlet (07.7 / 07.9)
BASELINE_MIN (ajánlott indulás):
CAP:REPO:READ_TREE
CAP:REPO:READ_FILE
CAP:REPO:APPLY_PATCH
CAP:DOC:WRITE_MD
CAP:VCS:DIFF
CAP:VCS:COMMIT (HIGH, governance gate-elt)
CAP:TEST:RUN (gyakran VERIFY)
CAP:SEARCH:WEB (ha elérhető; DYNAMIC)
Bővítés szabály: új CAP felvétele csak Decision + Review után, ha “rendszer-szintű”.
4.9 Handoff Manifest integráció (04 + 05 kompatibilis)
A HANDOFF_MANIFEST (04) használatakor MUST:
required_capabilities: [CAP:...]
capability_contract: (platformonként availability/confidence/validation_type)
capability_validation_tasks: (ha VERIFY/UNKNOWN)
required_return_evidence: [EVID:...]