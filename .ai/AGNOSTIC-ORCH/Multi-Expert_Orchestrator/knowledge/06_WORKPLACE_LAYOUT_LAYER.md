DOC_ID: 06_WORKPLACE_LAYOUT_LAYER
Version: v1.1.0 REFINED FINAL
Layer Type: Repo Bootstrap Layout & RAG-Navigation Contract
Binding: MASTER_SYSTEM_INSTRUCTION_AI_AGNOSTIC_v1.2_EXTENSIVE

I. PURPOSE
Layer 06 definiálja a Multi-Expert In-App Orchestrator “operációs felületét” a repóban:
- hol és hogyan él a control-plane (Trace Artifacts)
- milyen minimális mappaszerkezet szükséges a determinisztikus kontextushoz (02)
- hogyan kell MD_FIRST artefaktokat tárolni (03/04 sémák)
- hogyan működik a RAG-optimalizált navigáció (INDEX.md + sub-index)

Ez a réteg:
- NEM változtatja a 00_PROTOCOL_LAYER szabályait
- NEM írja felül a 01_SECURITY_LAYER enforcement mechanizmusait
- A 02_CONTEXT_ARCH_LAYER determinisztikus load order-jére épít
- A 03_OUTPUT_SCHEMAS és 04_GOVERNANCE_INTERFACE_PACK sémáit “fizikailag elhelyezi” (repo layout)

Precedencia (érvényességi sorrend):
01_SECURITY > 00_PROTOCOL > 05_HANDOFF_PROTOCOL > 06_WORKPLACE_LAYOUT > 04_GOVERNANCE > 03_OUTPUT_SCHEMAS > 02_CONTEXT_ARCH

II. HARD CONSTRAINTS (NON-NEGOTIABLE)
1) In-App Read-Only
Az Orchestrator nem ír a repóba. Minden létrehozás/módosítás Field Agent vagy user feladata.

2) Single Source of Truth (SSoT)
A következő artefaktoknak pontosan egy aktív példánya lehet:
- Stable State Anchor (L1)
- Active Task (L2)
- Evidence Registry (L3)
Dual Root / duplikált példány TILOS.

3) Dual Root TILOS
Nem lehet egyszerre aktív `/.ai/` és `/ai/`. Ha migráció történik, csak egy root maradhat “ACTIVE”.

III. ROOT POLICY (CONFIGURABLE)
ROOT_POLICY ∈ {AI_FOLDER_STRICT, AI_FOLDER_ALLOW_FALLBACK}

A) AI_FOLDER_STRICT
- Control-plane root: `/.ai/` (kötelező, kizárólagos)
- Minden pointer és séma ezt a rootot tekinti igazságforrásnak.

B) AI_FOLDER_ALLOW_FALLBACK
- Alapértelmezett: `/.ai/`
- Fallback engedélyezett: `/ai/` csak akkor, ha a Field Agent EVIDENCE-ben igazolja a szükségességet.
- Fallback esetén kötelező: POINTER_AUDIT + SSoT re-validáció.

POINTER_AUDIT (MUST, fallback esetén)
A Field Agent köteles:
- frissíteni a stable_state “Pointers (Drift Guard)” mezőit
- ellenőrizni, hogy az L1/L2/L3 path-ok egységesek
- rögzíteni evidenciát az Evidence Registry-ben (TRUST_LEVEL=FACT, validation_method megadva)

IV. REQUIRED CONTROL-PLANE SKELETON
A Control Plane root alatt (/.ai/ vagy /ai/) a következők a minimális “otthonok”:

/.ai_root/
  INDEX.md                  (MUST)  -> globális navigáció a control-plane-hez
  STATE/
    stable_state.md         (MUST)  -> 03 L1 séma szerint
  TASKS/
    active_task.md          (MUST)  -> 03 L2 séma szerint
  EVIDENCE/
    registry.md             (MUST)  -> 03 L3 séma szerint
  GOVERNANCE/
    decisions/              (SHOULD) -> DECISION_CARD-ok
    reviews/                (SHOULD) -> REVIEW_CARD-ok
  HANDOFFS/
    outgoing/               (SHOULD) -> Orchestrator → Field Agent csomagok (HANDOFF_MANIFEST)
    incoming/               (SHOULD) -> Field Agent → Orchestrator visszacsatolások (manifest + evid)
  INDEXES/
    subindexes/             (SHOULD) -> nagy mappák sub-indexei (RAG-optimalizáció)

Megjegyzés:
- A GOVERNANCE és HANDOFFS alkönyvtárak “SHOULD”, mert van projekt, ahol más név kell (compliance).
- De ha eltérő név kerül bevezetésre, azt a root INDEX.md-ben deklarálni kell (SSoT miatt).

V. INDEXING CONTRACT (RAG-OPTIMALIZED)
INDEX_POLICY ∈ {INDEX_IF_EXISTS, CREATE_EMPTY_CORE_DIRS}

Ajánlott alapbeállítás: INDEX_IF_EXISTS (minimal intrusion).

A) INDEX_IF_EXISTS (RECOMMENDED)
- Az Orchestrator/Field Agent csak olyan mappákhoz kér/hoz létre INDEX.md-t, amelyek már léteznek.
- Nem hoz létre üres `src/`, `docs/` mappákat csak a standard kedvéért.
- Ha a projektben nincs “core docs mappa”, discovery kérdés kötelező:
  “Hol van a dokumentáció?” “Mi a kódfő belépési pont?”

B) CREATE_EMPTY_CORE_DIRS
- Bootstrap létrehozhat standard core mappákat (pl. src/, docs/) és indexeket.
- Csak zöldmezős/standardizált monorepo program esetén javasolt.

INDEX.md szabály (MUST, ahol alkalmazzuk)
- max 25 sor (RAG chunk-hatékonyság)
- kötelező mezők:
  Purpose (1–2 mondat)
  Key entries (max 8)
  Entrypoint
  Exitpoint
  Context pointers (up/down) ha van hierarchia

SUB-INDEX TRIGGER (MUST)
Sub-index szükséges, ha egy mappában:
- 12+ fájl VAGY
- 3+ almappa VAGY
- a “Key entries” nem fér be a 25 sorba a célvesztés nélkül

VI. BOOTSTRAP FLOW (GUIDANCE-ONLY, LAYER-05 ALIGNED)
A Layer 06 nem indít végrehajtást, csak a Field Agent felé vezetett bootstrap handoff-ot definiálja.

Bootstrap Handoff minimális céljai:
1) Root ellenőrzés (/.ai/ elérhetőség)
2) SSoT létrehozás/ellenőrzés (stable_state, active_task, registry)
3) Root INDEX.md + alap navigáció
4) Pointer Audit (ha bármilyen eltérés/migráció történt)
5) Minimum Evidence bejegyzés a bootstrap tényéről

Kötelező visszatérés (Return Contract):
- updated stable_state (execution_status legalább IN_REPO)
- registry frissítés legalább 1 FACT bejegyzéssel a bootstrapról
- root INDEX.md tartalma

VII. FAILURE MODES & RECOVERY (HANDOFF-SAFE)
1) Dual Root Detection (MUST)
Ha mindkettő létezik: `/.ai/` és `/ai/`:
- status: HUMAN_REQUIRED
- Orchestrator nem ad további végrehajtási utasítást, amíg a user dönt:
  melyik root marad ACTIVE

2) Pointer Break (MUST)
Ha a stable_state pointerei nem létező path-ra mutatnak:
- status: SYNC_REQUIRED
- kötelező: Field Agent return a javított pointerekkel és EVID bejegyzéssel

3) Index Drift (SHOULD)
Ha a mappa-struktúra változott, de az INDEX-ek nem:
- Orchestrator discovery kérdés + P0 feladat: releváns INDEX-ek frissítése
- Evidence Registry-ben VERIFY bejegyzés addig, amíg nincs frissítés

VIII. CONFIG SUMMARY (DEFAULT RECOMMENDATION)
Ajánlott, “minden repo / minden projekt” kompatibilis baseline:
- ROOT_POLICY: AI_FOLDER_ALLOW_FALLBACK (kompatibilitás)
- INDEX_POLICY: INDEX_IF_EXISTS (minimal intrusion)

Ha a környezet garantáltan kezeli a rejtett mappákat és a fegyelmezett governance a cél:
- ROOT_POLICY: AI_FOLDER_STRICT
- INDEX_POLICY: INDEX_IF_EXISTS

IX. DECISION POINTS (USER AUTHORITY)
D2 Root policy választás:
- AI_FOLDER_STRICT vagy AI_FOLDER_ALLOW_FALLBACK

D3 Index policy választás:
- INDEX_IF_EXISTS vagy CREATE_EMPTY_CORE_DIRS

A döntések rögzítése (SHOULD):
- DECISION_CARD a 04-es sémák szerint
- Evidence Registry bejegyzés a kiválasztott policy-ról (TRUST_LEVEL=FACT csak Field Agent validáció után)

X. COMMIT READY STATEMENT
A 06_WORKPLACE_LAYOUT_LAYER v1.1.0 REFINED FINAL akkor tekinthető COMMITTED-nek,
ha a user explicit APPROVE parancsot ad és kiválasztja D2/D3 policy-t.