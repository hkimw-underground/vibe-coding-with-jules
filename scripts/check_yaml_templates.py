#!/usr/bin/env python3
"""Validate GitHub Issue Template YAML files without external dependencies."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
REQUIRED_KEYS = ("name:", "about:", "title:", "labels:", "body:")


def check_template(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not text.endswith("\n"):
        errors.append("file must end with a newline")

    for key in REQUIRED_KEYS:
        if not any(line.startswith(key) for line in lines):
            errors.append(f"missing top-level key `{key}`")

    for index, line in enumerate(lines, start=1):
        if "\t" in line:
            errors.append(f"line {index}: tabs are not allowed in YAML")
        leading_spaces = len(line) - len(line.lstrip(" "))
        if leading_spaces % 2 != 0:
            errors.append(f"line {index}: indentation should use multiples of two spaces")

    return errors


def main() -> int:
    failures: list[str] = []

    if not TEMPLATE_DIR.exists():
        print("No issue template directory found; skipping YAML template checks.")
        return 0

    templates = sorted(TEMPLATE_DIR.glob("*.yml")) + sorted(TEMPLATE_DIR.glob("*.yaml"))
    if not templates:
        failures.append("no YAML issue templates found")

    for path in templates:
        rel = path.relative_to(ROOT)
        for error in check_template(path):
            failures.append(f"{rel}: {error}")

    if failures:
        print("YAML template checks failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"YAML template checks passed for {len(templates)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
