---
name: node_orchestration
description: Expert-level Node.js, JS, and TS ecosystem management.
version: 1.0.0
category: development
---

# Skill: Node.js Orchestration

This skill provides the Field Agent with the capability to manage complex Node.js environments, enforce dependency integrity, and automate JavaScript/TypeScript project workflows.

## Context (Grounding)
- Consult `[ROOT]/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md`.
- Reference `npm audit` and `ag_npm_audit.py` for security baseline.

## Capabilities
1. **Environment Initialization**:
    - Manage `nvm` aliases and `node` versions.
    - Initialize `package.json` with standardized AntiGravity metadata.
2. **Dependency Management**:
    - Install and audit packages via `npm` or `yarn`.
    - Enforce the use of lockfiles (`package-lock.json`) for deterministic builds.
3. **Build & Script Orchestration**:
    - Automate `npm run build` and `npm test` cycles.
    - Scaffold TypeScript configurations (`tsconfig.json`) based on project requirements.
4. **Zero-Trust Verification**:
    - Run `ag_npm_audit.py` to check for unauthorized dependency patterns or scripts.

## Guidance for Generation
When creating new Node.js files (JS/TS/NJS):
- **Structure**: Always prefer a modular structure (e.g., `src/`, `tests/`, `dist/`).
- **Safety**: Ensure `node_modules/` is added to `.ai/tools/HARMONIZATION_RULES.json` exclude list (Mandatory).
- **Metadata**: Include `loop_id` and `agent_id` in `package.json` custom fields.

## Risks
- **Supply Chain Attacks**: Never install packages without a background audit.
- **Path Desync**: Use `[ROOT]` in scripts to maintain portable pathing logic.

## Knowledge Map
- **Governance**: [Protocol Layer](./.ai/AGNOSTIC-ORCH/knowledge/00_PROTOCOL_LAYER.md)
- **Tooling**: [NPM Audit Tool](./.ai/tools/ag_npm_audit.py)
- **Dashboards**: [Mission Control](./readme.html)
