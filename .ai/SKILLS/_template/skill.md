# SKILL (TEMPLATE) v0.1
skill_id: SKILL:TEMPLATE
version: 0.1
intent: Egy végrehajtható, újrafelhasználható rutin leírása (nem tool-call).
inputs_required:
- repo_root
- optional: external_sources
steps:
1. Discovery (csak read): releváns fájlok felderítése
2. Plan: minimál beavatkozás, csak szükséges módosítások
3. Output: javasolt patch vagy doc változás
validation:
- method: diff|doc|test
- expected_evidence: EVID:...
safety:
- no_repo_write_by_orchestrator: true
- external_sources_trust: UNTRUSTED_DATA_by_default
