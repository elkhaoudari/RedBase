# Payload Standard

Payload content will be added after the repository foundation is accepted.

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
