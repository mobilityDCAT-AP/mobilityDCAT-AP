#!/usr/bin/env python3
"""Build ReSpec spec to dist/index.html.

Uses respec's built-in --localhost server so data-include paths resolve
correctly.

index.html loads the NAPCORE ReSpec profile from src/js/respec-napcore.js,
a copy kept in the repository, so builds do not change when the published
profile does. The respec package pinned in package.json only drives the
headless browser; the profile does the rendering. --use-local is not passed:
it only replaces a ReSpec loaded from w3.org, which this page does not use.

TIMEOUT covers the whole run (browser launch, page load, rendering); respec's
default of 10 s is too short for this document.

In CI (the CI environment variable is set, as on GitHub Actions) the build
fails on any ReSpec error, for example when a reference lookup fails. Local
builds only report errors, so a missing network connection does not stop them.

Run from repo root: python src/scripts/build-spec.py [--verbose]
"""

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC = Path("src/index.html")    # relative — required by respec --localhost
OUT = Path("dist/index.html")   # relative — required by respec --localhost
TIMEOUT = 120                   # seconds


def main() -> None:
    (REPO_ROOT / OUT).parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "respec", "--localhost",
        "--timeout", str(TIMEOUT),
        "-s", str(SRC), "-o", str(OUT),
    ]
    if os.environ.get("CI"):
        cmd.append("--haltonerror")
    if "--verbose" in sys.argv:
        cmd.append("--verbose")

    result = subprocess.run(cmd, cwd=REPO_ROOT, shell=(sys.platform == "win32"))
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
