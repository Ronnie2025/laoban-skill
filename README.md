# Persona/Work Skill Methodology

Public methodology for turning raw human materials into reusable skills without publishing private identity details.

This repository documents a generic process for:

- ingesting raw materials such as transcripts, chat logs, notes, and docs
- extracting evidence-backed behavior and work patterns
- splitting output into `persona` and `work` layers
- maintaining an incremental correction and version loop
- exporting a public-safe methodology without leaking names, companies, paths, or private context

## Why This Exists

Most "act like this person" assets fail in one of two ways:

1. They are vivid but not grounded in evidence.
2. They are grounded in evidence but publish too much private detail.

This methodology is designed to avoid both failures.

## Core Principles

1. Evidence first
   Every stable conclusion should be traceable to raw material or explicitly marked as an inference.
2. Split persona from work
   Communication patterns and role behavior belong in different files from process rules and domain work habits.
3. Build a longitudinal memory layer
   Do not update the final prompt directly from raw material every time. Insert a history-memory layer between raw evidence and stable assets.
4. Separate stable patterns from one-off scenes
   Preserve cases and quotes for evidence, but promote only repeated patterns into the stable layer.
5. Treat correction as a first-class input
   User corrections are not comments. They are model-shaping data.
6. Sanitize by default
   Public export must remove names, orgs, products, internal shorthand, exact paths, and sensitive numbers.
7. Public and private artifacts are different products
   Private persona assets may exist, but public release should contain only the method, templates, and redaction rules.

## Pipeline

The recommended pipeline has six stages:

1. Intake
   Normalize sources and classify what kind of material each source is.
2. Evidence Extraction
   Extract behavior cases, quotes, work habits, terminology, and confidence signals.
3. History Memory
   Write one memory file per source or session to preserve evidence before compression.
4. Stable Assets
   Merge repeated patterns into `persona.md`, `work.md`, and optionally a `master-prompt.md`.
5. Correction and Versioning
   Add user corrections, detect conflicts, archive versions, and keep a rollback path.
6. Public Export
   Export only methodology, templates, and redaction-safe examples.

Detailed guidance:

- [Pipeline](docs/pipeline.md)
- [Sanitization](docs/sanitization.md)
- [Comparison With `colleague-skill`](docs/comparison-with-colleague-skill.md)

## What To Keep From `colleague-skill`

The public repository [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) is strong in four places:

- explicit `persona` / `work` split
- separate analyzer and builder stages
- correction handling
- version management

This methodology keeps those strengths and adds a transcript-first memory layer plus a stricter public-export boundary.

## Repository Layout

```text
.
├── README.md
├── docs/
│   ├── comparison-with-colleague-skill.md
│   ├── pipeline.md
│   └── sanitization.md
└── templates/
    ├── correction.md
    ├── history-memory.md
    ├── master-prompt.md
    ├── persona.md
    └── work.md
```

## When To Use This Method

Use this method when you need to:

- distill a manager, colleague, founder, operator, or domain expert into reusable AI behavior
- keep a durable private corpus while publishing only the framework
- continuously update the asset from new meetings or chats
- preserve evidence quality instead of writing a single large prompt

## When Not To Use It

Do not use this method if:

- you only need a one-off roleplay prompt
- you have no raw evidence and only vague impressions
- the public output is expected to contain real identities or internal details

## Start Point

If you are building this from scratch:

1. Start with [templates/history-memory.md](templates/history-memory.md).
2. Promote repeated patterns into [templates/persona.md](templates/persona.md) and [templates/work.md](templates/work.md).
3. Add corrections through [templates/correction.md](templates/correction.md).
4. Export a public-safe summary only after applying [Sanitization](docs/sanitization.md).
