# Sanitization

Sanitization is mandatory before any public release.

## Redaction Targets

Replace or remove:

- person names
- company names
- department names
- product names
- customer names
- project codenames
- private URLs
- local file paths
- exact numbers when they are sensitive
- internal shorthand that only makes sense inside one org

## Replacement Strategy

Use consistent placeholders when context matters:

- `Manager A`
- `Peer B`
- `Client C`
- `Product X`
- `System Y`
- `Workspace Z`

Use generic descriptions when the specific identity is not needed:

- `an internal review process`
- `a customer-facing workflow`
- `a production escalation meeting`

## Preserve Function, Remove Identity

Good sanitization keeps method and deletes traceability.

### Bad

- "When a named executive reviews Product X pricing requests, he says ..."
- "/absolute/private/path/notes/..."

### Good

- "When the subject reviews pricing-related requests, the pattern is to ask for scope, boundary, and monetization logic first."
- "private working directory"

## Numbers

Replace exact values when disclosure is risky:

- `17 customers` -> `a small but real customer set`
- `¥120,000` -> `a meaningful commercial amount`

Keep exact numbers only when they are non-sensitive and structurally important to the method.

## Quotes

Quotes are high-risk identifiers.

Public export should:

- prefer paraphrase over direct quote
- keep only generic, reusable phrasing
- remove distinctive wording that can fingerprint the person

## Safety Check Before Publishing

Run at least one keyword scan against:

- the subject's name
- company names
- client names
- product names
- usernames
- filesystem roots

Then do one manual pass to catch indirect identifiers.
