#!/usr/bin/env python3
"""Serialise the RDF/XML ontology (.rdf) to Turtle, JSON-LD and N-Triples.

RDF/XML is the source of the 1.1.0 ontology, as it was before this build:
src/mobilitydcat-ap.rdf is edited (for example in Protégé, with
catalog-v001.xml) and published as it is; copy-assets.py copies it. The
Turtle, JSON-LD and N-Triples are generated into dist/ on every build and are
never committed. The scripts of 1.1.0 did the same with rdfpipe
(serialise-vocabulary.sh).

Only the ontology is serialised. 1.1.0 publishes its examples as Turtle and
RDF/XML files that are both maintained by hand, and its SHACL shapes as Turtle
only; copy-assets.py copies them as they are.

Run from repo root: python src/scripts/serialise.py
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import rdflib
from rdflib.compare import isomorphic, to_canonical_graph

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# rdflib rewrites typed literals to its own canonical form when it parses
# them, e.g. "23:59:59.999"^^xsd:dateTime to "23:59:59.999000". Keep each
# literal exactly as written in the source.
rdflib.NORMALIZE_LITERALS = False

# The RDF/XML declares the ontology namespace twice, as the default namespace
# and as mobilitydcatap:, and the parser keeps only the default one. The other
# serialisations use the registered prefix, as the published 1.1.0 files did.
NAMESPACE_PREFIX = ("mobilitydcatap", "https://w3id.org/mobilitydcat-ap#")


def write(path: Path, text: str) -> None:
    """Write with LF endings, so Windows and CI produce identical files.

    Line breaks inside RDF literals are content: translating them to CRLF
    would change the data, not just the file.
    """
    path.write_text(text, encoding="utf-8", newline="\n")


def stable(g: rdflib.Graph) -> rdflib.Graph:
    """Return a copy of g that serialises the same way on every run.

    The parser gives blank nodes random names, and the serialisers write
    nodes in an order that depends on those names. Naming the blank nodes
    from their content and adding the triples in sorted order removes that.
    The rest of the order comes from Python sets, which main() fixes with
    PYTHONHASHSEED.
    """
    out = rdflib.Graph(bind_namespaces="none")
    for prefix, namespace in sorted(g.namespaces()):
        if prefix:
            out.bind(prefix, namespace)
    out.bind(*NAMESPACE_PREFIX, replace=True)
    for triple in sorted(to_canonical_graph(g), key=lambda t: [n.n3() for n in t]):
        out.add(triple)
    return out


def serialise(src: Path, out: Path) -> None:
    # Only the prefixes declared in the file, not rdflib's own (it would write
    # dcterms: for the dct: the 1.1.0 files use)
    g = stable(rdflib.Graph(bind_namespaces="none").parse(str(src), format="xml"))

    out.mkdir(parents=True, exist_ok=True)
    stem = src.stem

    ttl = g.serialize(format="turtle")
    if not isomorphic(g, rdflib.Graph().parse(data=ttl, format="turtle")):
        sys.exit(f"  {src.name}: Turtle does not round-trip")
    write(out / f"{stem}.ttl", ttl)

    raw = g.serialize(format="json-ld")
    jsonld = json.dumps(json.loads(raw), indent=2, ensure_ascii=False)
    write(out / f"{stem}.jsonld", jsonld)

    # One triple per line, sorted, so the file diffs line by line
    lines = g.serialize(format="nt").splitlines()
    nt = "".join(f"{line}\n" for line in sorted(set(lines)) if line)
    if not isomorphic(g, rdflib.Graph().parse(data=nt, format="nt")):
        sys.exit(f"  {src.name}: N-Triples does not round-trip")
    write(out / f"{stem}.nt", nt)

    print(f"  {src.name} -> {out.relative_to(REPO_ROOT) / stem}.(ttl|jsonld|nt)")


def main() -> None:
    # The serialisers iterate Python sets, whose order changes with the
    # string hash seed of each run. Run again with a fixed seed, so the
    # output only changes when the source does.
    if os.environ.get("PYTHONHASHSEED") != "0":
        env = {**os.environ, "PYTHONHASHSEED": "0"}
        sys.exit(subprocess.run([sys.executable, *sys.argv], env=env).returncode)

    dist = REPO_ROOT / "dist"

    print("== Serialise RDF/XML vocabulary ==")
    for f in sorted((REPO_ROOT / "src").glob("*.rdf")):
        serialise(f, dist)

    print("\nSerialise Done.")


if __name__ == "__main__":
    main()
