# SKILLSETS (INDEX)
Purpose: Generált vagy manuális skillset összeállítások tárhelye.
Key entries:
- active_skillset.md          -> A rendszer aktuálisan aktivált skillsetje
- active_skillset.generated.md -> A generátor szkript (skillset_gen.py) által automatikusan előállított változat, felülírás elleni védelemként a manuális fájl mellett.

Usage: 
Orchestrator loads `active_skillset.md` as priority. 
If auto-generated updates are available in `active_skillset.generated.md`, they must be manually reviewed before promoting to `active_skillset.md`.
