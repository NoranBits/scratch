# Skill: Data Breach Guard & Zero-Trust Security
**ID**: AG-SKILL-BREACH-GUARD
**Version**: 1.0.0
**Status**: ACTIVE
**Trust Level**: L10 (Guardian/Security)

## Context
External forked code and digestion processes can inadvertently introduce sensitive data (secrets, PII) or insecure patterns into the system. This skill mandates a zero-trust approach to all integrated logic.

## Capabilities
- **Secret Detection**: Automatic scanning for API keys, SSH keys, and environment variables.
- **PII Scrubbing**: Identifying personally identifiable information (emails, IPs) in logs or data structures.
- **Insecure Pattern Audit**: Detecting usage of dangerous functions (e.g., `eval`, `shell=True` without sanitization).
- **Pre-Publish Verification**: Mandatory final audit before repository publication.

## Expert Patterns

### 1. Zero-Trust Digestion
All paths designated for "digestion" must pass a security scan *before* being moved into the system core.
- **Requirement**: `ag_security_scanner.py --path external_repos/target_module`
- **Pass Criteria**: Zero HIGH or CRITICAL findings.

### 2. Secret Redaction
If a secret is found in a legitimate configuration file:
- **Pattern**: Replace literal values with references to a secure `.env` template or L0-L1 vault.

## Knowledge Map
- **Tooling**: [Security Scanner](./.ai/tools/ag_security_scanner.py)
- **Governance**: [Protocol Layer](./.ai/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md)
- **Digestion**: [Repo Digestion](./.ai/SAMPLES/SKILLS/skill_repo_digestion.md)
