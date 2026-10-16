#!/usr/bin/env python3
"""Copy source assets to dist/ before the ReSpec build.

Only hand-authored files are copied. The RDF/XML, JSON-LD and N-Triples
serialisations of the ontology are produced by serialise.py.

The directory names are the ones 1.1.0 was published with, so the URLs under
releases/1.1.0/ stay as they are.

Run from repo root: python src/scripts/copy-assets.py
"""

import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC = REPO_ROOT / "src"
DIST = REPO_ROOT / "dist"


def copy_glob(pattern: str, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for f in SRC.glob(pattern):
        shutil.copy2(f, dest / f.name)


def main() -> None:
    copy_glob("mobilitydcat-ap.ttl", DIST)

    for sub in ["examples", "figures", "shaclShapes", "enterpriseArchitectFiles"]:
        src_dir = SRC / sub
        if src_dir.exists():
            shutil.copytree(src_dir, DIST / sub, dirs_exist_ok=True)

    print("Assets copied to dist/")


if __name__ == "__main__":
    main()
