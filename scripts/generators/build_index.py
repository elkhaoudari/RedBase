#!/usr/bin/env python3
"""Build a deterministic JSON index from RedBase YAML records."""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[2]

def records_under(folder, kind):
    results = []
    if not folder.exists():
        return results
    for path in sorted(folder.rglob("*.yaml")):
        with path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        data["_record_type"] = kind
        data["_path"] = path.relative_to(ROOT).as_posix()
        results.append(data)
    return results

def main():
    techniques = records_under(ROOT / "knowledge", "technique")
    payloads = records_under(ROOT / "payloads", "payload")
    index = {
        "project": "RedBase",
        "index_schema_version": 1,
        "techniques": techniques,
        "payloads": payloads,
    }
    output = ROOT / "generated" / "index.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(index, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} ({len(techniques)} techniques, {len(payloads)} payloads).")

if __name__ == "__main__":
    main()
