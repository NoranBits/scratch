# FEDERATION & ORPHAN CONTEXT STRATEGY
**Schema ID**: `06_SCHEMA_FEDERATION_STRATEGY`
**Level**: Multi-Repo Coordination (L5/L6)

## 1. Orphaned Context Detection
A context is considered "Orphaned" if:
- It exists in an external root (e.g. `external_repos/repo_X/.ai/`)
- Its `stable_state` does not point to the central repository root as an Authority.
- It contains its own `peers.md` or `FEDERATION` layer without an active sync bridge.

## 2. Sync Bridge Protocol (Proposed)
To synchronize an orphaned repository like `repo_alpha`:

1. **Discovery (M1 Step)**: Identify the peer's loop_id and state hash.
2. **Intent Alignment**: The central Orchestrator generates an `INTENT_CARD` for the peer sync.
3. **Bridge Handshake**: 
   - Central `peers.md` adds `repo_alpha` as a trusted satellite.
   - `repo_alpha/.ai/FEDERATION/peers.md` is updated to point to the Central Repo as the Governance Source.
4. **Digest Mirroring**: Essential facts from the satellite are mirrored into the Central `registry.md` using `EVID:FED:...` prefix. 
   - **Mirror Schema**: `{satellite_id, satellite_root, satellite_loop_id, state_hash, captured_utc, source_peer_file}`.

## 3. Decision Points
- [ ] Shall satellites maintain independent `active_task.md` or inherit from the Central queue?
- [ ] Trust delegation: Can satellite-validated `FACTS` be promoted to the Central Repo without re-verification? (Standard recommendation: NO - Require Peer Review).
