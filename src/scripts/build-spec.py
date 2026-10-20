#!/usr/bin/env python3
"""Build ReSpec spec to dist/index.html.

Uses respec's built-in --localhost server so data-include paths resolve
correctly.

--use-local renders with the ReSpec bundle from node_modules (pinned in
package.json) instead of the live script referenced by index.html, so builds
do not change when w3.org publishes a new ReSpec version.

TIMEOUT is respec's --timeout: the time for the whole run, browser launch
included, but respec only enforces it on loading and rendering the page. Its
default of 10 s is too short for this document.

Starting the browser has a separate limit of 30 s, puppeteer's default, which
respec does not let us change. On a busy CI runner Chrome occasionally misses
it, so a run that fails while starting the browser is retried once. Any other
failure is not retried.

Run from repo root: python src/scripts/build-spec.py [--verbose]
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC = Path("src/index.html")    # relative — required by respec --localhost
OUT = Path("dist/index.html")   # relative — required by respec --localhost
TIMEOUT = 120                   # seconds
ATTEMPTS = 2

# Puppeteer's messages when Chrome does not start: it did not report that it
# was ready within the launch limit, or its process exited
LAUNCH_FAILURES = (
    "waiting for the WS endpoint URL",
    "Failed to launch the browser process",
)


def run(cmd: list[str]) -> tuple[int, bool]:
    """Run respec, passing its output through as it comes.

    Returns the exit code and whether the output shows a failed browser
    launch.
    """
    proc = subprocess.Popen(
        cmd, cwd=REPO_ROOT, shell=(sys.platform == "win32"),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    assert proc.stdout is not None   # set by stdout=PIPE
    launch_failed = False
    for line in proc.stdout:
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        text = line.decode("utf-8", errors="replace")
        if any(marker in text for marker in LAUNCH_FAILURES):
            launch_failed = True
    return proc.wait(), launch_failed


def main() -> None:
    (REPO_ROOT / OUT).parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "respec", "--localhost", "--use-local",
        "--timeout", str(TIMEOUT),
        "-s", str(SRC), "-o", str(OUT),
    ]
    if "--verbose" in sys.argv:
        cmd.append("--verbose")

    attempt = 1
    returncode, launch_failed = run(cmd)
    while returncode != 0 and launch_failed and attempt < ATTEMPTS:
        attempt += 1
        print(f"Chrome did not start; retrying ({attempt} of {ATTEMPTS})",
              flush=True)
        returncode, launch_failed = run(cmd)

    sys.exit(returncode)


if __name__ == "__main__":
    main()
