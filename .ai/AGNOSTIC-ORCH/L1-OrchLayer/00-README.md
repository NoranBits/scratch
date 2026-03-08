# OrchLayer GPT Documentation Pack

## Purpose

This package contains the documentation, knowledge files, setup guidance, starter prompts, and handoff materials for building and operating a **Project-first, Custom-GPT-backed L1 Orchestrator** inside ChatGPT.

The target operating model is:

- **Custom GPT** = stable operating kernel and reference knowledge
- **Projects** = long-running workspace and continuity layer
- **Session Packet / Handoff Package** = explicit portable continuity artifacts

---

## Included Files

- `00-README.md` — package overview and recommended usage
- `01-SYSTEM-OVERVIEW.md` — architecture, goals, and operating model
- `02-BUILDER-SETUP-GUIDE.md` — how to configure the Custom GPT in ChatGPT
- `03-KB-CORE-OPERATING-MODEL.md` — stable knowledge file
- `04-KB-SESSION-AND-HANDOFF.md` — stable knowledge file
- `05-KB-PATTERNS-AND-REVIEW.md` — stable knowledge file
- `06-STARTER-PROMPTS.md` — ready-to-use starter prompts
- `07-BUILDER-CHAT-FINETUNING.md` — builder chat refinement prompts and tuning workflow
- `08-NAMING-METADATA.md` — recommended name, description, metadata, and branding options
- `09-HANDOFF-CONTINUATION.md` — explicit handoff package for continuing this work

---

## Recommended Deployment Model

### Custom GPT
Use the Custom GPT for:
- identity
- behavior rules
- response mode selection
- drift control
- stable handoff/session behavior
- reference knowledge

### Project
Use a ChatGPT Project for:
- active files
- live conversations
- evolving requirements
- working documents
- long-running continuity

### Session Packet
Use Session Packets when:
- you may continue in another chat
- you want a compact checkpoint
- you want explicit continuity instead of relying on memory

### Handoff Package
Use Handoff Packages when:
- another person or AI needs a clean continuation brief
- you want to bootstrap a new chat
- you want portable execution or review context

---

## Recommended File Placement

### Upload to Custom GPT Knowledge
Upload these files as GPT Knowledge:
- `03-KB-CORE-OPERATING-MODEL.md`
- `04-KB-SESSION-AND-HANDOFF.md`
- `05-KB-PATTERNS-AND-REVIEW.md`

### Put into Project Workspace
Keep these as working/project documents:
- `01-SYSTEM-OVERVIEW.md`
- `02-BUILDER-SETUP-GUIDE.md`
- `06-STARTER-PROMPTS.md`
- `07-BUILDER-CHAT-FINETUNING.md`
- `08-NAMING-METADATA.md`
- `09-HANDOFF-CONTINUATION.md`

---

## Recommended Next Steps

1. Create the Custom GPT.
2. Set the final GPT name, description, and metadata.
3. Paste the builder instructions from `02-BUILDER-SETUP-GUIDE.md`.
4. Upload the 3 KB files.
5. Create or choose a Project for the active work.
6. Use starter prompts from `06-STARTER-PROMPTS.md`.
7. Use the handoff document to continue the refinement process.

---

## Design Principle

This package is optimized for:
- low drift
- clean scope control
- explicit continuity
- good Project compatibility
- practical Custom GPT usage inside ChatGPT

It is not optimized for pretending that the GPT has durable hidden memory across independent chats.
