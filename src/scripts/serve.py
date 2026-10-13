#!/usr/bin/env python3
"""Serve src/ over HTTP for live ReSpec preview.

Open the printed URL in a browser to see the live spec with
ReSpec's interactive warnings panel (broken references, lint issues, etc.).
A file missing from src/ is served from dist/ instead, so after a build the
links to the generated RDF/XML, JSON-LD and N-Triples files work too.
Stop with Ctrl+C.

Run from repo root: python src/scripts/serve.py
"""

import http.server
from pathlib import Path

PORT = 8080
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_DIR = REPO_ROOT / "src"
DIST_DIR = REPO_ROOT / "dist"


class _PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SRC_DIR), **kwargs)

    def translate_path(self, path):
        src_path = Path(super().translate_path(path))
        if src_path.exists():
            return str(src_path)
        # Generated files exist only in dist/; fall back to it
        dist_path = DIST_DIR / src_path.relative_to(SRC_DIR)
        return str(dist_path if dist_path.exists() else src_path)

    def log_message(self, format, *args):  # noqa: A002
        pass  # suppress per-request noise


def main() -> None:
    server = http.server.HTTPServer(("localhost", PORT), _PreviewHandler)

    print(f"Serving src/ (falling back to dist/) on http://localhost:{PORT}")
    print(f"Open in browser: http://localhost:{PORT}/")
    print("Stop with Ctrl+C")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
