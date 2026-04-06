# Comparison With `colleague-skill`

Reference repository: [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)

This file does not repeat that repository. It isolates the methodological gap.

## What `colleague-skill` Already Does Well

From its prompt and tool layout, `colleague-skill` already provides:

- an intake stage
- separate `persona` and `work` analyzers
- separate builders for final assets
- a correction handler
- incremental merge logic
- version management
- multiple collectors and parsers for chat and mail style sources

That is a strong asset-building pipeline.

## What A Transcript-Centered Method Adds

If your strongest raw material is transcripts or meeting records, there are four missing layers that should be made explicit:

### 1. History Memory Between Raw Material And Stable Assets

`colleague-skill` goes from source analysis toward stable files quickly.

A transcript-centered method benefits from an intermediate memory layer:

- one memory file per meeting or source
- evidence preserved before full compression
- case-level structure instead of only final traits

### 2. Confidence Management

Transcripts are noisy. Speaker labels, ASR quality, and context can all be wrong.

A stronger method should mark:

- explicit evidence
- inferred evidence
- low-confidence evidence that should not yet become a stable rule

### 3. Mandatory Sanitization For Public Export

`colleague-skill` is optimized for building a person skill.

A public methodology repo needs an additional layer:

- a rule set for stripping identity
- a public-only export pack
- examples that preserve method but not fingerprint

### 4. Longitudinal Compression

Repeated meetings create recurring patterns.

A stronger method should compress:

- repeated principles
- repeated questioning patterns
- repeated review heuristics

without discarding the evidence trail.

## What To Reuse

If you are building a public-safe variant, keep these ideas from `colleague-skill`:

- `persona` / `work` separation
- analyzer vs builder separation
- correction as structured data
- merge with conflict prompts
- version archive and rollback

## What To Add

Add these layers:

- transcript-aware history-memory template
- confidence labels
- sanitization checklist
- public/private export split
- stable-rule promotion rules

## Result

The final public method becomes:

`source intake -> evidence extraction -> history memory -> persona/work stable assets -> correction/versioning -> sanitized public export`

That is the core pattern this repository publishes.
