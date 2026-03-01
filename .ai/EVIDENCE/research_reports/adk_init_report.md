# ADK Initialization Research Report
**Status**: VERIFY
**Date**: 2026-02-28

**1. Discovery of in-repo documentation**
The Anti-Gravity IDE employs an "agent-first era" approach extending beyond traditional IDE functions. Discovery of in-repo documentation is designed around its flexible, code-first Agent Development Kit (ADK). Specifics regarding native `.ai` scanning require deeper verification, but the platform fundamentally emphasizes applying software development principles to agent creation, allowing direct ingestion of file structures.

**2. Required configuration files for `/.ai/` recognition**
Current high-level ADK documentation highlights its model-agnostic and deployment-agnostic nature. While optimized for the Google ecosystem, it does not explicitly mandate singular `.json` or `.yaml` manifests in public schemas for the `/.ai/` folder. It relies on programmatic definitions (code-first approach) for orchestration, making a hybrid or custom `/.ai/` bootstrap viable.

**3. Official way to define "Tools"**
ADK enables the "direct definition of agent logic, tools, and orchestration." Tools are defined programmatically as functions or structured capabilities that agents can trigger. This code-first tool definition emphasizes flexibility, testability, and versioning.
