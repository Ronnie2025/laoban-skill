# Pipeline

This pipeline is designed for evidence-backed persona/work skill building.

## 1. Intake

Input sources may include:

- meeting transcripts
- chat logs
- emails
- docs
- planning notes
- code reviews

For each source, record:

- source type
- date
- confidence level
- whether it is mostly persona, mostly work, or mixed
- whether it contains sensitive identifiers

Do not merge everything immediately. Keep source boundaries intact.

## 2. Evidence Extraction

Extract only what the source can support.

### Persona evidence

- repeated phrases
- questioning patterns
- tone and sentence rhythm
- reactions under pressure
- how disagreement is expressed
- behavior toward managers, peers, and reports

### Work evidence

- task intake habits
- review criteria
- decision rules
- process expectations
- output structure
- operating checklists

### Confidence labels

Each extracted observation should be tagged with a confidence level:

- high: directly supported by repeated or explicit evidence
- medium: clearly supported once, but not yet repeated
- low: plausible inference that should not become a stable rule yet

## 3. History Memory

Before updating the stable layer, write a history-memory file per source or session.

History memory has two jobs:

1. Preserve evidence without over-compressing it.
2. Create a safe staging area before stable rules are updated.

Recommended contents:

- source metadata
- sanitized background
- 2-5 high-value cases
- key quotes or phrasing
- abstracted method points
- a fixed-dimension summary for later merging

Use [templates/history-memory.md](../templates/history-memory.md).

## 4. Stable Assets

Only repeated, durable patterns should move into stable assets.

### `persona.md`

Should contain:

- core behavior rules
- tone and expression patterns
- decision and disagreement style
- relationship behavior
- boundaries and red lines

### `work.md`

Should contain:

- scope and responsibility boundaries
- work intake and review flow
- output templates
- prioritization rules
- operational heuristics

### Optional `master-prompt.md`

Useful when you need a compact execution surface for an agent, but it should be downstream of `persona.md` and `work.md`, not a replacement for them.

## 5. Merge Logic

When new material arrives:

- append new evidence to history memory
- compare against existing stable rules
- add new stable patterns only when evidence is repeated or clearly confirmed
- surface conflicts instead of silently overwriting

Never overwrite a stable rule just because a single new source sounds different.

## 6. Correction Loop

User corrections should be captured structurally:

- scene
- wrong behavior
- correct behavior
- target file: persona or work
- whether it overrides or only refines an existing rule

Corrections should update the stable layer and be archived as a change event.

Use [templates/correction.md](../templates/correction.md).

## 7. Versioning

Every stable update should produce:

- a version label
- a short update summary
- archived previous files
- a rollback path

The goal is not only traceability. It is preventing drift.

## 8. Public Export

Public export is a separate stage, not a visibility toggle.

Public output should include:

- methodology
- templates
- generic examples
- sanitization rules

Public output should exclude:

- real names
- employer or client names
- internal product names
- internal shorthand
- local file paths
- exact sensitive figures
- distinctive quotes that can identify the subject

See [Sanitization](sanitization.md).
