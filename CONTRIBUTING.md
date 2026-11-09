# Contributing to RedBase

## Before contributing

- Search the existing taxonomy and IDs to avoid duplicate entries.
- Prefer one canonical record with cross-references over copied duplicates.
- Clearly distinguish original work from adapted material.
- Check the source license before adapting or redistributing content.
- Do not claim testing or verification without evidence.

## Technique contribution checklist

- [ ] Markdown explanation and sibling YAML metadata are both present.
- [ ] ID is unique, stable, lowercase kebab-case.
- [ ] Category and subcategory match the taxonomy.
- [ ] References are specific and attributable.
- [ ] `source` and `license` accurately describe provenance.
- [ ] If adapted, `adapted_from` is populated and license compatibility is checked.
- [ ] Defensive considerations are included.
- [ ] Validation passes.

## Payload contribution checklist (for a later phase)

- [ ] Unique payload ID.
- [ ] Valid `technique_id` reference.
- [ ] Context, target technology, and encoding are described where applicable.
- [ ] Expected behavior is explained.
- [ ] Provenance and license are recorded.
- [ ] Verification claims have evidence.

## Pull requests

Keep PRs focused. Explain what category is being added, why it is not a duplicate, which sources support it, and any license constraints.
