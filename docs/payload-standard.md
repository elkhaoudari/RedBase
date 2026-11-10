# Payload Standard

Payload records are stored as structured YAML and linked to technique records.

## Storage model

- Store payloads as structured YAML records.
- Each payload has one canonical immutable ID and one canonical record.
- Link records to techniques using `technique_id`.
- Put context, technology, version, encoding, and applicability in metadata.
- Do not copy the same record into multiple directories for discoverability.
- Group files by vulnerability family and useful context only where that helps maintenance.

## Recommended fields

- `id`
- `schema_version`
- `technique_id`
- `name`
- `content`
- `target_technology`
- `technology_versions`
- `injection_context`
- `encoding`
- `expected_behavior`
- `waf_bypass_for`
- `related_payload`
- `review`
- `references`
- `source`
- `adapted_from`
- `license`

Context and encoding values should be controlled vocabularies where practical, but allow documented extensions for new cases.

## Payload licensing and provenance

- Original RedBase payload records use `CC-BY-4.0` for their authored prose and
  record structure, consistent with the project's original documentation policy.
- The payload `content` field is commonly a protocol example or placeholder; cite
  the relevant standard or technical reference and do not claim ownership of
  third-party material.
- Adapted payload records must retain a compatible upstream license, identify
  the source in `adapted_from`, and include attribution. If redistribution rights
  are unclear or incompatible, link to the source instead of copying it.
- `pending-policy-review` is a temporary holding value used by this initial SSRF
  batch. Resolve it before treating these records as release-ready.
