#!/usr/bin/env python3
"""Mark dist/index.html as a draft, after the ReSpec build.

Adds a notice at the top of the page, a "Draft" badge that stays in the corner
while scrolling and links to the notice, and a "Draft: " prefix to the title.
src/config.js keeps the values of the release a draft prepares, so without the
notice a draft looks like a release.

CI runs it for every build except a release (see reusable-build.yml).
DRAFT_LABEL says what the build is, for example "the working draft" or "draft
snapshot 3.0.0-draft.1"; the commit and the date are added to it. It is an
environment variable, not an argument, because mise does not quote task
arguments on Windows.

Run from repo root after a build:
    DRAFT_LABEL="the working draft" python src/scripts/mark-draft.py
"""

import html
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PAGE = REPO_ROOT / "dist" / "index.html"
LATEST_RELEASE_URL = "https://w3id.org/mobilitydcat-ap"
DEFAULT_LABEL = "a local build of the draft"

# Foreground and background are both set, so the notice stays readable whatever
# colours the page itself uses
STYLE = """<style id="draft-notice-style">
#draft-notice { margin: 1em 0 2em; padding: 0.8em 1em; border: 2px solid #b35900;
  border-radius: 4px; background: #fff4e5; color: #3d2400; }
#draft-notice a { color: #8a4500; }
#draft-badge { position: fixed; top: 0; right: 0; z-index: 1000; padding: 0.3em 0.8em;
  background: #b35900; color: #fff; font-weight: bold; text-decoration: none;
  border-bottom-left-radius: 4px; }
</style>
"""


def commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def notice(what: str) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return (
        '<a id="draft-badge" href="#draft-notice">Draft</a>\n'
        '<div id="draft-notice" role="note">\n'
        f"<p><strong>This is {html.escape(what)}</strong>, built from commit "
        f"<code>{commit()}</code> on {today}. It is not a release, and its "
        "content can still change before the release. The version, status and "
        "links in the header below describe the release this draft prepares.</p>\n"
        f'<p>The current release is at <a href="{LATEST_RELEASE_URL}">'
        f"{LATEST_RELEASE_URL}</a>.</p>\n"
        "</div>\n"
    )


def main() -> None:
    label = os.environ.get("DRAFT_LABEL", "").strip() or DEFAULT_LABEL
    page = PAGE.read_text(encoding="utf-8")
    if 'id="draft-notice"' in page:
        sys.exit(f"{PAGE} already has a draft notice")

    page, n_title = re.subn(r"<title>", "<title>Draft: ", page, count=1)
    page, n_head = re.subn(r"</head>", lambda m: STYLE + m.group(0), page, count=1)
    page, n_body = re.subn(
        r"<body[^>]*>", lambda m: m.group(0) + "\n" + notice(label),
        page, count=1,
    )
    if not (n_title and n_head and n_body):
        sys.exit(f"{PAGE}: no <title>, </head> or <body> to mark")

    PAGE.write_text(page, encoding="utf-8")
    print(f"Marked {PAGE.relative_to(REPO_ROOT)} as {label}")


if __name__ == "__main__":
    main()
