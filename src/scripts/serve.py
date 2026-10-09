#!/usr/bin/env python3
"""Serve the repo over HTTP for live ReSpec preview.

Open the printed URL in a browser to see the live spec with
ReSpec's interactive warnings panel (broken references, lint issues, etc.).
Stop with Ctrl+C.

Run from repo root: python src/scripts/serve.py
"""

import functools
import http.server
from pathlib import Path

PORT = 8080
REPO_ROOT = Path(__file__).resolve().parent.parent.parent


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002
        pass  # suppress per-request noise


def main() -> None:
    handler = functools.partial(_QuietHandler, directory=str(REPO_ROOT))
    server = http.server.HTTPServer(("localhost", PORT), handler)

    print(f"Serving on http://localhost:{PORT}")
    print(f"Open in browser: http://localhost:{PORT}/src/index.html")
    print("Stop with Ctrl+C")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
