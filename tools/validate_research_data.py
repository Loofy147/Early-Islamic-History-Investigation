#!/usr/bin/env python3
"""Structural validation of research registers; does not authenticate sources or historical truth."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "data/sources/source_register.csv": "source_id",
    "data/claims/claim_register.csv": "claim_id",
    "data/events/event_register.csv": "event_id",
    "data/hypotheses/hypothesis_register.csv": "hypothesis_id",
}
ALLOWED = {"FACT", "ESTABLISHED", "REPORTED", "INFERENCE", "HYPOTHESIS", "DISPUTED", "UNKNOWN", "CONTRADICTED"}


def main() -> int:
    errors: list[str] = []
    for relative, id_column in FILES.items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing file: {relative}")
            continue
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream, strict=True)
                if not reader.fieldnames or id_column not in reader.fieldnames:
                    errors.append(f"missing header/column {id_column}: {relative}")
                    continue
                expected_columns = len(reader.fieldnames)
                seen: set[str] = set()
                for line, row in enumerate(reader, start=2):
                    if None in row:
                        errors.append(
                            f"{relative}:{line}: row has extra fields; check unquoted commas"
                        )
                        continue
                    if len(row) != expected_columns:
                        errors.append(f"{relative}:{line}: expected {expected_columns} fields, got {len(row)}")
                        continue
                    value = (row.get(id_column) or "").strip()
                    if not value:
                        errors.append(f"{relative}:{line}: empty {id_column}")
                    elif value in seen:
                        errors.append(f"{relative}:{line}: duplicate {id_column}={value}")
                    seen.add(value)
                    status = (row.get("status") or "").strip()
                    if relative.endswith("claim_register.csv") and status not in ALLOWED:
                        errors.append(f"{relative}:{line}: invalid claim status {status!r}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{relative}: {exc}")

    if errors:
        print("\n".join(errors))
        return 1
    print("VALIDATION PASSED: required registers, row widths, IDs and claim statuses are structurally valid.")
    print("This check does not authenticate sources or verify historical claims.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
