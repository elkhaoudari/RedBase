# RedBase Architecture

## 1. Product definition

RedBase is a long-lived, Git-based reference collection for Web and API security techniques and (in a later phase) structured payload records. Its primary objective is breadth of coverage while retaining stable identifiers, traceable provenance, and consistent metadata.

## 2. Locked decisions

| Concern | Decision |
|---|---|
| Initial domain | Web + API security |
| Priority | Coverage |
| Source of truth | Git repository |
| Documentation | Markdown |
| Metadata | YAML |
| Technique organization | Grouped by vulnerability/category |
| Payload storage | Structured YAML |
| Licensing | Mixed, according to content type and upstream rights |
| Database/backend/GUI | Out of current scope |
| Labs | Out of current scope |
| Payload population | Later phase |

## 3. Repository layers

- **Knowledge layer (`knowledge/`)**: one Markdown explanation paired with one YAML metadata file for each technique.
- **Payload layer (`payloads/`)**: reserved for structured payload records. It is intentionally empty in this architecture phase.
- **Schema layer (`schemas/`)**: machine-readable contracts for technique and payload records.
- **Automation layer (`scripts/`)**: local validation and deterministic index generation.
- **Reference layer (`references/`)**: curated source register and reference policy.
- **Generated layer (`generated/`)**: derived JSON index, never a source of truth.

## 4. Canonical record model

A technique has:
- one immutable `id`;
- one Markdown explanation;
- one sibling YAML metadata file;
- zero or more payload references;
- zero or more related technique IDs.

A payload (introduced later) has:
- one immutable payload `id`;
- one structured YAML record;
- exactly one canonical record;
- one or more technique references only where the schema explicitly supports them.

Cross-cutting properties such as framework, context, encoding, and WAF applicability belong in metadata, not duplicated directory trees.

## 5. Grouping and paths

Technique records are grouped by domain/category/subcategory. Individual techniques are paired files in a group:

```text
knowledge/
  web/
    injection/
      sqli/
        web-injection-sqli-union-based.md
        web-injection-sqli-union-based.yaml
```

Payload records will be grouped by vulnerability family and optionally by useful technical context, but metadata remains authoritative. Do not duplicate a payload into multiple folders to make it discoverable.

## 6. Trust model

Review states:
- `unverified`: not technically reviewed or tested.
- `reviewed`: content reviewed for correctness, but not necessarily executed.
- `verified`: tested in a controlled, authorized environment with evidence and version details.
- `deprecated`: retained for historical context but no longer recommended.

A `verified` record must include a date, tested-against details, and evidence references. Verification is not inferred from a successful YAML validation.

## 7. Build and validation flow

1. Parse YAML.
2. Validate records against JSON Schema.
3. Enforce globally unique IDs.
4. Validate technique and payload cross-references.
5. Enforce verification and provenance rules.
6. Generate a deterministic index only after validation passes.

## 8. Explicit non-goals for this phase

No database, hosted API, web GUI, payload runner, vulnerability scanner, Docker lab system, or populated payload corpus.
