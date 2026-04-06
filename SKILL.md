---
name: create-boss
description: Distill a reusable boss skill from transcripts, meeting notes, chat logs, and documents. Use when the user wants to capture a manager's review style, decision logic, meeting habits, and execution push style into persona/work assets with incremental updates.
---

# 老板.skill

Use this skill to create or update a boss-style skill from raw materials.

## Inputs

- meeting transcripts
- chat logs
- docs or notes written by the subject
- user descriptions and corrections

## Outputs

- `history memory` files for source-level evidence
- `work.md` for stable working method
- `persona.md` for stable expression and behavior style
- optional `master-prompt.md` for compact execution

## Default Workflow

1. Run [prompts/intake.md](prompts/intake.md) to collect context and define the target role.
2. For each major source, use [prompts/history_memory_builder.md](prompts/history_memory_builder.md) to produce a memory layer before compression.
3. Merge repeated work patterns into [templates/work.md](templates/work.md) using [prompts/work_builder.md](prompts/work_builder.md).
4. Merge repeated speaking and behavior patterns into [templates/persona.md](templates/persona.md) using [prompts/persona_builder.md](prompts/persona_builder.md).
5. If the user wants a compact execution surface, build `master-prompt.md` with [prompts/master_prompt_builder.md](prompts/master_prompt_builder.md).
6. For new material, apply [prompts/merger.md](prompts/merger.md).
7. For user corrections, apply [prompts/correction_handler.md](prompts/correction_handler.md).

## Working Rules

- Treat transcripts and long-form material as the highest-value sources.
- Preserve evidence before compressing it into stable rules.
- Separate `persona` from `work`.
- Prefer repeated patterns over one-off moments.
- When new material conflicts with stable rules, surface the conflict instead of silently overwriting.

## Generated Skill Layout

```text
bosses/{slug}/
├── persona.md
├── work.md
├── master-prompt.md
├── meta.json
└── versions/
```
