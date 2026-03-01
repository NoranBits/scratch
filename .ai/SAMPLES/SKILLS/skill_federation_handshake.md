---
name: federation_handshake
description: Securely bridging orphaned contexts into the central registry.
version: 0.9.0
category: multi-repo
---

# Skill: Federation Handshake

This skill manages the discovery and integration of external repositories (Satellites) into the central authority.

## Context (Grounding)
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/05_HANDOFF_PROTOCOL_LAYER.md`.
- Reference `FEDERATION_STRATEGY.md`.

## Capabilities
1. **Satellite Discovery**: Inspect `external_repos/` for valid `.ai/` root structures.
2. **Bridge Negotiation**: Propose a handshake to the Orchestrator when an orphaned `peers.md` is detected.
3. **Fact Mirroring**: Aggregating `stable_state` hashes from satellites into the central `registry.md` as `EVID:FED` entries.

### Mirror Schema (Mandatory Fields)
Every `EVID:FED` mirror entry MUST include:
- `satellite_id`: Canonical name of the external repo.
- `satellite_root`: Absolute or relative path to the satellite root.
- `satellite_loop_id`: The last active loop ID of the satellite.
- `state_hash`: The L1 `stable_state` anchor hash from the satellite.
- `captured_utc`: ISO 8601 timestamp of the mirror event.
- `trust`: Always starts at `VERIFY`.
- `source_peer_file`: Path to the `peers.md` that triggered the discovery.

## Risks
- **Data Leakage**: Do not pull satellite code into central memory without explicit `HANDOFF_MANIFEST` authorization.
- **Trust Desync**: Satellites are `VERIFY` by default; do not promote their facts to `FACT` without central audit.
