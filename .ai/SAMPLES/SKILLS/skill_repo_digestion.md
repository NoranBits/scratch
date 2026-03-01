# Skill: Repository Digestion & Selective Integration
**ID**: AG-SKILL-REPO-DIGEST
**Version**: 1.0.0
**Status**: ACTIVE
**Trust Level**: L9 (Architect/System)

## Context
In a large-scale MAS, cloning entire external repositories is often inefficient and introduces technical debt. "Digestion" is the act of selectively extracting high-value components (skills, tools, or logic) from a fork and integrating them into the system core with full provenance.

## Capabilities
- **Selective Extraction**: Identifying specific file paths or modules in `external_repos/` that align with current mission goals.
- **Provenance Linkage**: Maintaining a link back to the source repository for future synchronization.
- **Transformation Pipeline**: Applying necessary protocol transforms (e.g., namespace changes, governance headers) during integration.
- **Manifest Management**: Registration of digested components in `digestion_manifest.json`.

## Expert Patterns

### 1. Digestion Protocol
1.  **Identify**: Locating a capability in a forked peer (e.g., `external_repos/repo_alpha/src/logic/`).
2.  **Audit**: Running `ag_security_scanner.py` on the target path.
3.  **Extract**: Using `ag_repo_digester.py` to pull the logic into `src/` or `.ai/SKILLS/`.
4.  **Register**: Updating the manifest with source URL, commit hash, and local target.

### 2. Upstream Consistency
Digested code is "borrowed" logic. If the upstream fork updates:
- **Rescan**: Re-run digestion if a breaking change is detected in the upstream head.
- **Patch**: Apply localized fixes to the digested copy if the upstream is unstable.

## Knowledge Map
- **Security**: [Data Breach Guard](./.ai/SAMPLES/SKILLS/skill_data_breach_guard.md)
- **Tooling**: [Repo Digester](./.ai/tools/ag_repo_digester.py)
- **Federation**: [Git Federation](./.ai/SAMPLES/SKILLS/skill_git_federation_expert.md)
