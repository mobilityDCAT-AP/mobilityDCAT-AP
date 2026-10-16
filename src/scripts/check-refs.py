#!/usr/bin/env python3
"""Check for broken local references in dist/index.html.

Parses the built HTML, collects all id attributes and internal href="#..."
links, then reports any href that has no matching id.
Run from repo root: python src/scripts/check-refs.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DIST_INDEX = REPO_ROOT / "dist" / "index.html"


def main() -> None:
    if not DIST_INDEX.exists():
        print("dist/index.html not found — run 'mise run build' first.")
        sys.exit(1)

    html = DIST_INDEX.read_text(encoding="utf-8")

    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', html))
    hrefs = re.findall(r'\bhref=["\']#([^"\']+)["\']', html)

    counts: dict[str, int] = {}
    for h in hrefs:
        if h not in ids:
            counts[h] = counts.get(h, 0) + 1

    if not counts:
        print("No broken local references found.")
        sys.exit(0)

    total = sum(counts.values())
    print(f"Broken local references: {len(counts)} unique targets, {total} total occurrences")
    for ref, n in sorted(counts.items()):
        print(f"  #{ref}  ({n}x)")
    sys.exit(1)


if __name__ == "__main__":
    main()
