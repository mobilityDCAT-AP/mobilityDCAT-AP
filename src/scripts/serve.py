#!/usr/bin/env python3
"""Serve src/ over HTTP for live ReSpec preview, or dist/ with --dist.

Open the printed URL in a browser to see the live spec with
ReSpec's interactive warnings panel (broken references, lint issues, etc.).
A file missing from src/ is served from dist/ instead, so after a build the
links to the generated RDF/XML, JSON-LD and N-Triples files work too.

With --dist it serves only dist/, the built spec as it will be published,
on a second port so both can run side by side (requires a prior build).
Stop with Ctrl+C.

Run from repo root: python src/scripts/serve.py [--dist]
"""

import argparse
import functools
import http.server
import sys
from pathlib import Path

PORT = 8080
DIST_PORT = 8081
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_DIR = REPO_ROOT / "src"
DIST_DIR = REPO_ROOT / "dist"


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002
        pass  # suppress per-request noise


class _PreviewHandler(_QuietHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SRC_DIR), **kwargs)

    def translate_path(self, path):
        src_path = Path(super().translate_path(path))
        if src_path.exists():
            return str(src_path)
        # Generated files exist only in dist/; fall back to it
        dist_path = DIST_DIR / src_path.relative_to(SRC_DIR)
        return str(dist_path if dist_path.exists() else src_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the spec over HTTP for a preview.")
    parser.add_argument("--dist", action="store_true", help="serve the built dist/ instead")
    args = parser.parse_args()

    if args.dist:
        if not (DIST_DIR / "index.html").exists():
            sys.exit("dist/index.html not found; run mise run build first")
        port = DIST_PORT
        handler = functools.partial(_QuietHandler, directory=str(DIST_DIR))
        print(f"Serving dist/ on http://localhost:{port}")
    else:
        port = PORT
        handler = _PreviewHandler
        print(f"Serving src/ (falling back to dist/) on http://localhost:{port}")

    server = http.server.HTTPServer(("localhost", port), handler)

    print(f"Open in browser: http://localhost:{port}/")
    print("Stop with Ctrl+C")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
