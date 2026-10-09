#!/usr/bin/env python3
"""Copy source assets to dist/ before the ReSpec build.

Only hand-authored files are copied. The RDF/XML and JSON-LD serialisations of
the ontology, the examples and the SHACL shapes are produced by serialise.py.

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
    for sub in ["examples", "figures", "shaclShapes"]:
        (DIST / sub).mkdir(parents=True, exist_ok=True)

    copy_glob("mobilitydcat-ap.ttl", DIST)

    for f in (SRC / "examples").iterdir():
        if f.is_file():
            shutil.copy2(f, DIST / "examples" / f.name)

    for sub in ["figures", "shaclShapes", "migrationGuide"]:
        src_dir = SRC / sub
        if src_dir.exists():
            shutil.copytree(src_dir, DIST / sub, dirs_exist_ok=True)

    print("Assets copied to dist/")


if __name__ == "__main__":
    main()
