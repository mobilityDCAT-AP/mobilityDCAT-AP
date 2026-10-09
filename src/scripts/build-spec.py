#!/usr/bin/env python3
"""Build ReSpec spec to dist/index.html.

Uses respec's built-in --localhost server so data-include paths resolve
correctly.

--use-local renders with the ReSpec bundle from node_modules (pinned in
package.json) instead of the live script referenced by index.html, so builds
do not change when w3.org publishes a new ReSpec version.

TIMEOUT covers the whole run (browser launch, page load, rendering); respec's
default of 10 s is too short for this document.

Run from repo root: python src/scripts/build-spec.py [--verbose]
"""

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
        "respec", "--localhost", "--use-local",
        "--timeout", str(TIMEOUT),
        "-s", str(SRC), "-o", str(OUT),
    ]
    if "--verbose" in sys.argv:
        cmd.append("--verbose")

    result = subprocess.run(cmd, cwd=REPO_ROOT, shell=(sys.platform == "win32"))
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
