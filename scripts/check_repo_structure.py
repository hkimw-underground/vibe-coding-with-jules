#!/usr/bin/env python3
"""Check that the starter kit keeps its expected reusable structure."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "README.md",
    "README.ko.md",
    "AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/jules_task.yml",
    ".github/ISSUE_TEMPLATE/workflow_experiment.yml",
    "docs/workflows/workflow-levels.md",
    "docs/experiments/no-human-only-jules-workflow.md",
    "docs/experiments/jules-alpha-evolve.md",
    "prompts/issue-to-jules-task.md",
    "prompts/daily-maintainer-report.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]

    if missing:
        print("Repository structure checks failed:")
        for path in missing:
            print(f"- missing {path}")
        return 1

    print(f"Repository structure checks passed for {len(REQUIRED_PATHS)} required paths.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
