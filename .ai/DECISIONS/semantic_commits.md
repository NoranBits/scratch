# AntiGravity Semantic Commit Standard (AG-SCS)

To maintain architectural integrity across the 7-phase release lifecycle, all commits must follow the semantic structure below. This ensures the `ag_git_pulse.py` and `ag_release_nexus.py` tools can accurately track health and automate promotions.

## Message Format

```text
<type>(<scope>): <short_summary>

- Rationale: <reasoning_behind_change>
- Loop-ID: <active_cortex_loop_id>
- Impact: <high/med/low>
```

## Authorized Types

- **feat**: New architectural component or tool.
- **fix**: Resolution of a logic bug or neural misalignment.
- **chore**: Maintenance tasks (e.g., dependency updates, documentation).
- **refactor**: Code restructuring without functional changes.
- **docs**: Documentation-only changes (e.g., updates to `readme.html`).
- **test**: Adding or correcting verification suites.
- **release**: Automated phase promotion via `ag_release_nexus`.

## Phase Transition Requirements

| From | To | Requirement |
| :--- | :--- | :--- |
| **dev** | **demos** | All "Plan" items in `task.md` marked `[x]`. |
| **demos** | **alphas** | Successful walkthrough validation in `TEMP`. |
| **alphas** | **betas** | Security audit (GPG check) passed. |
| **betas** | **production** | Direct user approval and `vX.X.X` tagging. |

## Enforcement
The `ag_git_manager.py` tool will automatically prompt for these fields when using the `--commit` flag.
