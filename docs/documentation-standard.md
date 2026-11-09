# Documentation Standard

Each technique uses a paired `.md` and `.yaml` file with the same basename.

Required Markdown sections:

1. Overview — concise definition and impact class.
2. Technical explanation — how the weakness arises.
3. Detection — black-box and/or white-box indicators where applicable.
4. Contexts and variations — relevant input locations, platforms, and variants.
5. Related techniques — canonical IDs, not duplicated explanations.
6. Defensive considerations — detection, prevention, and mitigation.
7. References — specific, attributable sources.

Keep explanations concise and useful. Payloads belong in the structured payload collection, not copied into multiple technique documents.

A section may say "not applicable" with a short reason when the concept genuinely does not apply.
