#!/usr/bin/env python3
"""Validate RedBase YAML records and cross-references."""
from pathlib import Path
import sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"
KNOWLEDGE = ROOT / "knowledge"
PAYLOADS = ROOT / "payloads"

def load_yaml(path):
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            raise ValueError("YAML document must contain one mapping/object.")
        return data
    except Exception as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: {exc}") from exc

def load_schema(name):
    import json
    with (SCHEMAS / name).open(encoding="utf-8") as f:
        return json.load(f)

def validate_records(paths, schema_name, kind, errors):
    schema = load_schema(schema_name)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    records = []
    for path in sorted(paths):
        try:
            data = load_yaml(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for error in validator.iter_errors(data):
            loc = ".".join(str(x) for x in error.absolute_path)
            errors.append(f"{path.relative_to(ROOT)} [{loc}]: {error.message}")
        records.append((path, data))
    return records

def check_review(data, label, errors):
    review = data.get("review", {})
    if review.get("status") == "verified":
        if not review.get("last_tested"):
            errors.append(f"{label}: verified requires review.last_tested")
        if not review.get("tested_against"):
            errors.append(f"{label}: verified requires review.tested_against")
        if not review.get("evidence"):
            errors.append(f"{label}: verified requires review.evidence")

def check_provenance(data, label, errors):
    if data.get("source") == "adapted" and not data.get("adapted_from"):
        errors.append(f"{label}: source=adapted requires adapted_from")

def main():
    errors = []
    tech_paths = list(KNOWLEDGE.rglob("*.yaml")) if KNOWLEDGE.exists() else []
    payload_paths = list(PAYLOADS.rglob("*.yaml")) if PAYLOADS.exists() else []

    techniques = validate_records(tech_paths, "technique.schema.json", "technique", errors)
    payloads = validate_records(payload_paths, "payload.schema.json", "payload", errors)

    ids = {}
    technique_ids = set()
    payload_ids = set()

    for path, data in techniques:
        label = str(path.relative_to(ROOT))
        rid = data.get("id")
        if rid in ids:
            errors.append(f"{label}: duplicate ID {rid} (already used in {ids[rid]})")
        else:
            ids[rid] = label
        technique_ids.add(rid)
        check_review(data, label, errors)
        check_provenance(data, label, errors)

    for path, data in payloads:
        label = str(path.relative_to(ROOT))
        rid = data.get("id")
        if rid in ids:
            errors.append(f"{label}: duplicate ID {rid} (already used in {ids[rid]})")
        else:
            ids[rid] = label
        payload_ids.add(rid)
        check_review(data, label, errors)
        check_provenance(data, label, errors)
        if data.get("technique_id") not in technique_ids:
            errors.append(f"{label}: unknown technique_id {data.get('technique_id')}")

    for path, data in payloads:
        label = str(path.relative_to(ROOT))
        ref = data.get("related_payload")
        if ref is not None and ref not in payload_ids:
            errors.append(f"{label}: unknown related_payload {ref}")

    for path, data in techniques:
        label = str(path.relative_to(ROOT))
        for ref in data.get("related_techniques", []):
            if ref not in technique_ids:
                errors.append(f"{label}: unknown related_technique {ref}")
        for ref in data.get("payload_refs", []):
            if ref not in payload_ids:
                errors.append(f"{label}: unknown payload_ref {ref}")

    if errors:
        print("RedBase validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"RedBase validation passed: {len(techniques)} techniques, {len(payloads)} payloads.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
