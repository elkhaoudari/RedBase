# Metadata Standard

## Technique metadata

Each technique YAML file must follow `schemas/technique.schema.json`.

Core fields:
- `id`: immutable, lowercase kebab-case identifier.
- `schema_version`: metadata schema version.
- `name`, `description`: canonical name and concise description.
- `domain`, `category`, `subcategory`: taxonomy placement.
- `aliases`: alternative names.
- `target_technologies`: technologies, frameworks, databases, or platforms.
- `technology_versions`: known version constraints; empty when unknown or not applicable.
- `requirements`: prerequisites and applicability conditions.
- `payload_refs`: canonical payload IDs (empty until payloads are added).
- `related_techniques`: canonical technique IDs.
- `classification`: optional CWE/OWASP references.
- `tags`: cross-cutting search terms.
- `maturity`: `core`, `advanced`, or `research`.
- `review`: status, test date, tested-against values, and evidence.
- `source`, `adapted_from`, `license`: provenance.

## ID rules

- Lowercase kebab-case.
- IDs are globally unique across techniques and payloads (separate namespaces are also acceptable only if consistently enforced; RedBase uses global uniqueness).
- Never change an ID after merge. Use aliases or redirects for renamed concepts.
- Do not encode volatile version numbers into IDs.

## Verification rules

`verified` requires:
- `last_tested` as an ISO date;
- non-empty `tested_against`;
- non-empty evidence references.

`reviewed` means reviewed for technical accuracy, not necessarily executed.
