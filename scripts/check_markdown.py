#!/usr/bin/env python3
"""Lightweight Markdown sanity checks for the starter kit."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "node_modules", ".venv", "venv"}


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    if text and not text.endswith("\n"):
        errors.append("file must end with a newline")

    fence_count = 0
    for index, line in enumerate(lines, start=1):
        stripped_newline = line.rstrip("\n")
        if stripped_newline.endswith(" ") or stripped_newline.endswith("\t"):
            errors.append(f"line {index}: trailing whitespace")
        if stripped_newline.lstrip().startswith("```"):
            fence_count += 1

    if fence_count % 2 != 0:
        errors.append("unclosed fenced code block")

    return errors


def main() -> int:
    failures: list[str] = []
    files = markdown_files()

    if not files:
        failures.append("no Markdown files found")

    for path in files:
        rel = path.relative_to(ROOT)
        for error in check_file(path):
            failures.append(f"{rel}: {error}")

    if failures:
        print("Markdown checks failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Markdown checks passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
