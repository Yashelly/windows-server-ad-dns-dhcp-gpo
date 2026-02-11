#!/usr/bin/env python3
"""Lightweight repository consistency checks.

Goal: catch obvious issues before publishing.
- Required top-level files exist.
- Module folders follow NN-name pattern.
- Evidence folders exist.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "START-HERE.md",
    "STATUS.md",
    "baseline-manifest.yml",
]

MODULE_RE = re.compile(r"^(\d{2})-[a-z0-9-]+$")

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def main() -> None:
    for f in REQUIRED_FILES:
        if not (ROOT / f).exists():
            fail(f"Missing required file: {f}")

    modules = []
    for p in ROOT.iterdir():
        if p.is_dir() and MODULE_RE.match(p.name):
            modules.append(p.name)

    if not modules:
        fail("No module folders found (expected like 00-overview, 01-...).")

    ev = ROOT / "99-evidence"
    if not ev.exists():
        fail("Missing 99-evidence folder.")

    for sub in ["screenshots", "exports", "logs"]:
        if not (ev / sub).exists():
            print(f"WARN: 99-evidence/{sub} is missing")

    print("OK: basic checks passed")

if __name__ == "__main__":
    main()
