#!/usr/bin/env python3
"""Serialise the Turtle ontology (.ttl) to RDF/XML, JSON-LD and N-Triples.

Turtle is the source of truth. The RDF/XML, JSON-LD and N-Triples
serialisations are generated into dist/ on every build and are never
committed.

Only the ontology is serialised. 1.1.0 publishes its examples as Turtle and
RDF/XML files that are both maintained by hand, and its SHACL shapes as Turtle
only; copy-assets.py copies them as they are.

Run from repo root: python src/scripts/serialise.py
"""

import json
import os
import subprocess
import sys
import warnings
from io import BytesIO
from pathlib import Path

import rdflib
from rdflib import RDF, BNode, Literal
from rdflib.collection import Collection
from rdflib.compare import isomorphic, to_canonical_graph
from rdflib.plugins.serializers.rdfxml import RDFVOC, PrettyXMLSerializer

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# rdflib rewrites typed literals to its own canonical form when it parses
# them, e.g. "23:59:59.999"^^xsd:dateTime to "23:59:59.999000". Keep each
# literal exactly as written in the Turtle.
rdflib.NORMALIZE_LITERALS = False


class LiteralListXMLSerializer(PrettyXMLSerializer):
    """rdflib's pretty RDF/XML, with lists of literals written correctly.

    pretty-xml writes every list as rdf:parseType="Collection", which can only
    hold resources. A list of literals (sh:languageIn in the SHACL shapes) is
    then written as resources and lost. This writes such a list as nested
    rdf:first/rdf:rest blank nodes instead. It also keeps the other lists from
    being written twice, and leaves everything else to rdflib.

    It relies on rdflib internals (the private record of serialised nodes) and
    was written against rdflib 7.6.0. serialise() checks the result by round
    trip, so a change in rdflib makes the output flat, not wrong.
    """

    def predicate(self, predicate, object, depth=1):
        serialised = self._PrettyXMLSerializer__serialized
        if (
            isinstance(object, BNode)
            and object not in serialised
            and (object, RDF.first, None) in self.store
            and any(isinstance(i, Literal) for i in Collection(self.store, object))
        ):
            serialised[object] = 1
            self.writer.push(predicate)
            self.writer.attribute(RDFVOC.parseType, "Resource")
            self.predicate(RDF.first, self.store.value(object, RDF.first), depth + 1)
            self.predicate(RDF.rest, self.store.value(object, RDF.rest), depth + 1)
            self.writer.pop(predicate)
        else:
            new = object not in serialised
            super().predicate(predicate, object, depth)
            # rdflib marks only the first cell of a list it writes as a
            # Collection. Its last pass can then write another cell again,
            # as a stray list, so mark the rest of the cells too.
            if new and object in serialised and (object, RDF.rest, None) in self.store:
                node = self.store.value(object, RDF.rest)
                while isinstance(node, BNode) and node not in serialised:
                    serialised[node] = 1
                    node = self.store.value(node, RDF.rest)


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
        out.bind(prefix, namespace)
    for triple in sorted(to_canonical_graph(g), key=lambda t: [n.n3() for n in t]):
        out.add(triple)
    return out


def serialise(src: Path, out: Path) -> None:
    g = stable(rdflib.Graph().parse(str(src)))

    out.mkdir(parents=True, exist_ok=True)
    stem = src.stem

    # rdflib warns about every list it writes as a Collection, including the
    # correct ones. The warnings are silenced because the round trip below is
    # the actual check: if it fails, fall back to the flat serialiser.
    buf = BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        LiteralListXMLSerializer(g).serialize(buf, encoding="utf-8")
    rdf = buf.getvalue().decode("utf-8")
    if not isomorphic(g, rdflib.Graph().parse(data=rdf, format="xml")):
        rdf = g.serialize(format="xml")
        print(f"  {src.name}: pretty RDF/XML loses triples, using flat RDF/XML")
    write(out / f"{stem}.rdf", rdf)

    raw = g.serialize(format="json-ld")
    jsonld = json.dumps(json.loads(raw), indent=2, ensure_ascii=False)
    write(out / f"{stem}.jsonld", jsonld)

    # One triple per line, sorted, so the file diffs line by line
    lines = g.serialize(format="nt").splitlines()
    nt = "".join(f"{line}\n" for line in sorted(set(lines)) if line)
    if not isomorphic(g, rdflib.Graph().parse(data=nt, format="nt")):
        sys.exit(f"  {src.name}: N-Triples does not round-trip")
    write(out / f"{stem}.nt", nt)

    print(f"  {src.name} -> {out.relative_to(REPO_ROOT) / stem}.(rdf|jsonld|nt)")


def main() -> None:
    # The serialisers iterate Python sets, whose order changes with the
    # string hash seed of each run. Run again with a fixed seed, so the
    # output only changes when the Turtle does.
    if os.environ.get("PYTHONHASHSEED") != "0":
        env = {**os.environ, "PYTHONHASHSEED": "0"}
        sys.exit(subprocess.run([sys.executable, *sys.argv], env=env).returncode)

    dist = REPO_ROOT / "dist"

    print("== Serialise Turtle vocabulary ==")
    for f in sorted((REPO_ROOT / "src").glob("*.ttl")):
        serialise(f, dist)

    print("\nSerialise Done.")


if __name__ == "__main__":
    main()
