#!/usr/bin/env python3
"""Validate the examples against the mobilityDCAT-AP SHACL shapes.

The shapes are the four constraint files in src/shaclShapes/. What they
owl:imports is fetched once and kept in .cache/shacl/, so later runs work
offline:

- imports of mdr-imports.ttl are the controlled vocabularies. They are added
  to the data graph, because the membership checks look up skos:inScheme on
  the values.
- any other import that contains SHACL shapes is added to the shapes graph:
  the DCAT-AP 3.0.1 base shapes and deprecated URIs.
- the DCAT-AP range.ttl, imported by ranges.ttl, is left out unless
  --with-dcat-ap-ranges is given. Its sh:class checks need an explicit type on
  every value, which the EU authority tables do not provide (they type their
  concepts only as skos:Concept), so on the examples it reports every
  codelist value.
- plain vocabularies are not used: validation runs without inference, since
  RDFS inference over DCAT 2 makes every dcat:Catalog a dcat:Dataset.

Only results on nodes of the validated file are reported; the controlled
vocabularies in the data graph are reference data, not subject to validation.

Exits 1 if any file has a sh:Violation. Warnings and infos are printed only.

Run from repo root: python src/scripts/validate-examples.py [--offline]
    [--refresh] [--with-dcat-ap-ranges] [file.ttl ...]
"""

import argparse
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

import rdflib
from pyshacl import validate
from rdflib import OWL, RDF, Graph, Namespace

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SHAPES_DIR = REPO_ROOT / "src" / "shaclShapes"
EXAMPLES_DIR = REPO_ROOT / "src" / "examples"
CACHE_DIR = REPO_ROOT / ".cache" / "shacl"

SH = Namespace("http://www.w3.org/ns/shacl#")

SHAPE_FILES = ["shapes.ttl", "ranges.ttl", "mdr-vocabularies.ttl", "deprecated-uris.ttl"]
VOCABULARY_IMPORTS = "mdr-imports.ttl"
BASE_IMPORTS = "imports.ttl"
RANGE_FILE = "ranges.ttl"

# The EU authority tables answer with text/xml, which rdflib does not map to a
# parser, so the format is chosen here rather than left to rdflib.
FORMATS = {
    "text/turtle": "turtle",
    "application/x-turtle": "turtle",
    "application/n-triples": "nt",
    "application/rdf+xml": "xml",
    "text/xml": "xml",
    "application/xml": "xml",
    "application/ld+json": "json-ld",
}
HEADERS = {
    "Accept": "text/turtle, application/rdf+xml;q=0.9, application/n-triples;q=0.8, */*;q=0.1",
    # dublincore.org answers 403 to the default Python-urllib agent
    "User-Agent": "mobilitydcat-ap-validate-examples",
}


def cache_path(url: str) -> Path:
    return CACHE_DIR / (re.sub(r"[^A-Za-z0-9.-]+", "_", url.split("://", 1)[-1]) + ".nt")


def download(url: str) -> Graph:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
        ctype = resp.headers.get_content_type()
    # Trying Turtle on RDF/XML makes rdflib log a warning per line, so sniff first
    sniffed = "xml" if data.lstrip().startswith(b"<") else "turtle"
    tried = [FORMATS.get(ctype, sniffed)]
    tried += [f for f in (sniffed, "turtle", "xml") if f not in tried]
    for fmt in tried:
        try:
            return Graph().parse(data=data, format=fmt)
        except Exception:
            pass
    raise ValueError(f"not parseable as RDF (Content-Type {ctype})")


def missing_effect(declared_in: str) -> str:
    """What a missing import means for the results, by the file declaring it."""
    if declared_in == VOCABULARY_IMPORTS:
        return "codelist missing: every membership check against it fails"
    if declared_in == BASE_IMPORTS:
        return "results affected only if it holds shapes; vocabularies are not used"
    return "shapes missing: their constraints are not applied"


def load_import(url: str, declared_in: str, offline: bool, refresh: bool) -> Graph | None:
    """Return the imported graph, from the cache when possible, or None."""
    path = cache_path(url)
    if path.exists() and not refresh:
        return Graph().parse(path, format="nt")
    if offline:
        print(f"  not cached, skipped: {url}")
        print(f"         declared in {declared_in}; {missing_effect(declared_in)}")
        return None
    try:
        g = download(url)
    except Exception as e:
        print(f"  FAILED {url}: {e}")
        print(f"         declared in {declared_in}; {missing_effect(declared_in)}")
        return None
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    g.serialize(path, format="nt", encoding="utf-8")
    print(f"  fetched {len(g):>6} triples  {url}")
    return g


def imports_of(file_name: str) -> list[str]:
    g = Graph().parse(SHAPES_DIR / file_name)
    return sorted(str(o) for o in g.objects(None, OWL.imports))


def has_shapes(g: Graph) -> bool:
    return any(g.triples((None, RDF.type, SH.NodeShape))) or any(
        g.triples((None, RDF.type, SH.PropertyShape))
    )


def build_graphs(args) -> tuple[Graph, Graph]:
    shapes = Graph()
    for name in SHAPE_FILES:
        shapes.parse(SHAPES_DIR / name)

    print("== Load imports ==")
    vocabularies = Graph()
    for url in imports_of(VOCABULARY_IMPORTS):
        g = load_import(url, VOCABULARY_IMPORTS, args.offline, args.refresh)
        if g is not None:
            vocabularies += g

    for name in SHAPE_FILES + [BASE_IMPORTS]:
        for url in imports_of(name):
            if name == RANGE_FILE and not args.with_dcat_ap_ranges:
                print(f"  left out (see --with-dcat-ap-ranges): {url}")
                continue
            g = load_import(url, name, args.offline, args.refresh)
            if g is not None and has_shapes(g):
                shapes += g
    return shapes, vocabularies


def show(node) -> str:
    if node is None:
        return ""
    if isinstance(node, rdflib.BNode):
        return "[blank node]"
    return str(node)


def report(path: Path, shapes: Graph, vocabularies: Graph) -> int:
    """Validate one file, print its results, return the number of violations."""
    example = Graph().parse(path)
    own = set(example.subjects())

    _, results, _ = validate(
        example + vocabularies,
        shacl_graph=shapes,
        inference="none",
        do_owl_imports=False,
        allow_warnings=True,
    )

    rows = []
    for r in results.subjects(RDF.type, SH.ValidationResult):
        focus = results.value(r, SH.focusNode)
        if focus not in own:
            continue
        value = results.value(r, SH.value)
        rows.append((
            str(results.value(r, SH.resultSeverity)).split("#")[-1],
            show(focus),
            show(results.value(r, SH.resultPath)),
            show(value) if value != focus else "",
            str(results.value(r, SH.resultMessage) or ""),
        ))

    order = {"Violation": 0, "Warning": 1, "Info": 2}
    rows.sort(key=lambda row: (order.get(row[0], 3),) + row[1:])
    counts = Counter(row[0] for row in rows)

    rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else path
    summary = ", ".join(
        f"{counts[s]} {s.lower()}{'s' if counts[s] > 1 else ''}" for s in order if counts[s]
    )
    print(f"\n== {rel}: {summary or 'no results'} ==")
    for severity, focus, rpath, value, message in rows:
        print(f"  {severity:9} {focus}")
        if rpath:
            print(f"            path  {rpath}")
        if value:
            print(f"            value {value}")
        print(f"            {message}")
    return counts["Violation"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the examples against the SHACL shapes.")
    parser.add_argument("files", nargs="*", type=Path,
                        help="Turtle files to validate (default: src/examples/*.ttl)")
    parser.add_argument("--offline", action="store_true",
                        help="use only cached imports, never download")
    parser.add_argument("--refresh", action="store_true",
                        help="download every import again, replacing the cache")
    parser.add_argument("--with-dcat-ap-ranges", action="store_true",
                        help="also apply the DCAT-AP 3.0.1 range.ttl")
    args = parser.parse_args()

    files = [f.resolve() for f in args.files] or sorted(EXAMPLES_DIR.glob("*.ttl"))
    shapes, vocabularies = build_graphs(args)

    violations = sum(report(f, shapes, vocabularies) for f in files)
    if violations:
        print(f"\n{violations} violation(s).")
        sys.exit(1)
    print("\nNo violations.")


if __name__ == "__main__":
    main()
