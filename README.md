# RedBase
### The Offensive Security Payload Collection

RedBase is a long-term, Git-based knowledge base for organized Web and API security techniques, payload references, and supporting research.

**Current phase: architecture and repository foundation. Payload collection comes later.**

## Project principles

- Coverage-oriented taxonomy for Web and API security.
- Markdown for human-readable explanations; YAML for structured metadata.
- Structured payload records with stable IDs (content will be added in a later phase).
- Git is the source of truth; generated indexes are derived artifacts.
- No database, backend, GUI, Docker labs, or payload execution in the current scope.
- Never label content `verified` without documented test evidence.
- Preserve source attribution and comply with upstream licenses.

## Repository map

| Path | Purpose |
|---|---|
| `knowledge/` | Technique descriptions and paired YAML metadata |
| `payloads/` | Future structured payload collections |
| `docs/` | Architecture, taxonomy, metadata and contribution standards |
| `schemas/` | JSON Schemas for structured records |
| `scripts/` | Validation and deterministic index generation |
| `references/` | Curated external references and source register |
| `generated/` | Machine-generated index; never edit by hand |
| `tools/` | Future local utilities such as encoders/decoders |

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validators/validate.py
python scripts/generators/build_index.py
```

## Adding content

1. Read `docs/documentation-standard.md`, `docs/metadata-standard.md`, and `docs/payload-standard.md`.
2. Choose the canonical taxonomy location from `docs/taxonomy.md`.
3. Copy templates from `templates/`.
4. Assign immutable, unique IDs.
5. Record source and license provenance.
6. Run validation before opening a pull request.

## Scope boundaries

RedBase is a reference collection, not an exploitation framework or scanner. Content should support authorized security research, education, and testing. Do not add live-target credentials, private data, or target-specific weaponization.
