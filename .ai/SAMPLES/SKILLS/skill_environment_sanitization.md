# Skill: Environment Sanitization & Path Portability
**ID**: AG-SKILL-ENV-SAN
**Version**: 1.0.0
**Status**: ACTIVE
**Trust Level**: L10 (Guardian/Security)

## Context
A primary risk in agentic development is the accidental inclusion of local environment signatures (e.g., machine-specific absolute paths, username-linked directories) in shared or public repositories. This skill mandates strict path portability and sanitization.

## Capabilities
- **Relative Path Enforcement**: Ensuring that all internal links, references, and tool mappings use relative paths (`./` or `../`) anchored to the repository root.
- **Environment Signature Masking**: Identifying and neutralizing strings that reveal local system architecture or user identifiers.
- **Publish-Ready Auditing**: Mandatory use of `ag_env_sanitizer.py` before any commit to non-local branches.

## Expert Patterns

### 1. Absolute Path Neutralization
- **Bad**: `./readme.html`
- **Good**: `./readme.html` or `../readme.html`
- **Logic**: Use the current working directory or a centralized `REPO_ROOT` anchor to resolve paths dynamically within tools.

### 2. Sanitization Pipeline
Before "Digestion" or "Publication":
1.  **Scan**: Run `ag_security_scanner.py --detect-paths`.
2.  **Scrub**: Run `ag_env_sanitizer.py` to replace absolute clusters with relative markers.
3.  **Verify**: Re-run the scan to ensure a "Clean State."

## Knowledge Map
- **Security**: [Data Breach Guard](file:///./.ai/SAMPLES/SKILLS/skill_data_breach_guard.md)
- **Tooling**: [Env Sanitizer](file:///./.ai/tools/ag_env_sanitizer.py)
- **Governance**: [Protocol Layer](file:///./.ai/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md)
