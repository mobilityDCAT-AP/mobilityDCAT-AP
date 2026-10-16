#!/usr/bin/env python3
"""Empty dist/ before a fresh build.

Run from repo root: python src/scripts/clean.py
"""

import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DIST = REPO_ROOT / "dist"


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    print("dist/ cleared")


if __name__ == "__main__":
    main()
