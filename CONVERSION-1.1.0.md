# Conversion of release 1.1.0 to the build system

How the 1.1.0 sources on `release/1.1.0` were converted to the build and
publishing tooling of `main`, so that the conversion can be reviewed and
retraced. How to build and publish is in `DEVELOPMENT.md`.

## Starting point

| Ref | Commit | Role |
|-----|--------|------|
| `release/1.1.0` | `fc6cb37` | Base: the repository when 1.1.0 was the current release, identical to `gh-pages` at that commit |
| `main` | `d79e21d` | Source of the build tooling and workflows |
| `gh-pages` | `0481f3e` (2026-10-13) | Published state the result was compared against |
| `mobilityDCAT-AP/respec-style` | `7d3eef5` (2023-07-14) | Source of the NAPCORE ReSpec profile |

## Which source was used

`release/1.1.0` held several copies of 1.1.0 that had drifted apart:

| Copy | What it was | Used as |
|------|-------------|---------|
| `drafts/1.1.0-draft-0.1/` | The ReSpec source, with later edits that were never published (e.g. `e0cd0c9`) | **The source**, moved to `src/` |
| `releases/index.html` and the root of `releases/` | The rendered page, edited by hand afterwards; the most up-to-date copy; where w3id.org redirects `/releases/` and `/releases/latest/` | Reference for the page; its extra assets were copied |
| `releases/1.1.0/` | An older rendered copy that lacks some of those hand edits and its `figures/`; where w3id.org redirects `/releases/1.1.0/` | Reference only |
| `drafts/latest/` | The 3.0.0 draft | Not used |

The ontology and the examples were the same in all three 1.1.0 copies, the
SHACL shapes too apart from line endings (CRLF in the draft).

## File changes

- **Moved:** `drafts/1.1.0-draft-0.1/` → `src/`, with the ontology renamed
  `src/mobilitydcat-ap.rdf`. `src/shaclShapes/` and
  `src/enterpriseArchitectFiles/` keep their names, which are part of the
  published URLs (on `main` the SHACL directory is `src/shacl/`).
- **Removed:** the old `.sh` and `.php` build scripts; `src/README.md`, which
  pointed at the 3.0.0 draft; the Turtle and JSON-LD of the ontology, which are
  now generated (see [Ontology source](#ontology-source)).
- **Copied from the root of `releases/`**, because a publish empties its target
  directory and would otherwise remove them from `releases/latest/`: three
  figures, the Enterprise Architect documentation page and its `readme.md`
  (from `d9b51c4`). `releases/1.1.0/enterpriseArchitectFiles/mobilityDCAT-AP.qea`
  differs from the root copy by one inserted byte and was not used.
- **Copied from `main` unchanged:** `package.json`, `package-lock.json` (respec
  36.0.0, html-validate 10.13.1), `.python-version`, `.gitattributes`,
  `.htmlvalidate.json`, `.gitignore`, `check-refs.py`, `clean.py`,
  `mark-draft.py`, `serve.py`, `build-check.yml`, `build-release.yml`,
  `reusable-publish-gh-pages.yml`.
- **Copied from `main` and adapted:**
  - `serialise.py` serialises only the ontology, from RDF/XML to Turtle,
    JSON-LD and N-Triples; the examples and SHACL shapes are published as they
    are.
  - `copy-assets.py` copies `mobilitydcat-ap.rdf`, `examples/`, `figures/`,
    `shaclShapes/` and `enterpriseArchitectFiles/`.
  - `build-spec.py` drops `--use-local`, which only replaces a ReSpec loaded
    from w3.org, and adds `--haltonerror` when `CI` is set.
  - `pyshacl`, the `validate-examples` task and the SHACL cache steps of
    `reusable-build.yml` are removed: only `validate-examples.py` used them.
- **Not copied:** `validate-examples.py` (written for the 3.0.0 shapes, which
  import DCAT-AP 3.0.1; the 1.1.0 shapes import 2.0.1), `build-main.yml`,
  `build-draft.yml`, `promote-latest.yml` (they never fire from a release
  branch), `REPOSITORY.md` and `PROCEDURES.md` (they stay on `main`).
- **Line endings:** the 1.1.0 SHACL shapes in `src/shaclShapes/` and the four
  1.0.x SHACL files were renormalised from CRLF to LF; nothing else changed.
- **New documents:** `DEVELOPMENT.md`, `AGENTS.md` and `CLAUDE.md`; the
  repository structure in `README.md` describes this branch.

## NAPCORE ReSpec profile

The page loaded `respec-napcore.js` live from `mobilityDCAT-AP/respec-style`.
`src/js/respec-napcore.js` is now a copy of it at `7d3eef5` (ReSpec 25.16.5),
loaded by `src/index.html`, with a header comment and two changes:

- `RE:"Recommendation"` is added to the status labels. The published page was
  rendered with `specStatus: "RE"`, which the profile has no label for, and the
  header and status sentence were then fixed by hand.
- The bibliography is looked up at api.specref.org instead of
  specref.herokuapp.com, which answers 404. With the old URL, 17 references read
  "Reference not found." and 30 of the 53 links to sections of other
  specifications have no target.

Undoing the two changes and removing the comment gives a file byte-identical
to upstream. The stock ReSpec in `package.json` cannot replace the profile: it
would change the header and status text.

`src/config.js` gets the values the published page shows: `specStatus: "RE"`,
and `canonicalURI` and `prevRecURI` set to `releases/1.1.0/`.

## Matching the published page

The build is compared with the published root page, `releases/index.html`,
including its typos; no correction of 1.1.0 is made here.

Hand edits of the published page, ported to the source:

| Published edit | Fix in the source |
|----------------|-------------------|
| Copyright holder NAPCORE, linked to napcore.eu (`212a349`, since the 1.0.0 page) | `src/index.html`: a `<p class="copyright">`, which the profile uses instead of its "European Union" |
| "Reviewed by" and "Approved by" (`dcfe219`, since the 1.0.0 page) | `src/config.js`: `otherLinks` entries |
| Daham Mohammed Mustafa as first editor, and in the list of editors of the ReSpec documentation (`faf4ed9`) | `src/config.js`: first in `editors` (`ef494ac` had added him last); `src/index.html`: first in the list |
| Release date in the document history (`56dd3e7`) | `src/tables/document-history.html`: `17/01/2025` |
| Stray `-->`, `>` and `#">intended information service<` (#164: `8f829c7`, `8ba434a`) | Removed in `src/index.html`, `class-category-scheme.html`, `optional-properties-for-dataset.html` |
| Wording of the Annex G list of SHACL files (#178: `8b0c12e`) | `src/index.html` |

The source already had the agent-table order of `c690a85` and the
content-negotiation links of `8154676`. One fix has no published counterpart:
the Mobility Data Standard class table was missing from a build of the source,
because its `data-include` lacked `.html`.

Unpublished edits of the source, undone:

| Source edit | Undone |
|-------------|--------|
| `e0cd0c9`: "of the (NAPCORE) [NAPCORE] consortium" | "of the NAPCORE project [NAPCORE] consortium" |
| `e0cd0c9`: typos `[[RDF-SCHEMA]]]` and `[[EU-EIP-CMC]].)` corrected | The typos are restored |
| `e0cd0c9`: link around "described" in the privacy considerations removed | `<a data-cite="VOCAB-ODRL#privacy-consideration">` restored |
| `e0cd0c9`: a `[DCAT]` reference to DCAT 3 added | Removed |
| `e0cd0c9`: publisher of `[DXWG]`, `[GLD]`, `[Web-Annotation-Data-Model]`, `[VOCAB-DCAT-QA]` changed to "World Wide Web Consortium. W3C" | "W3C" |
| `ae0aa96`: three SHACL entries in the alternate formats | One entry, "SHACL (Turtle)" → `./shaclShapes/`, as published (`8b0c12e`) |

Specref, looked up at build time, has changed since the release: `[DCAT-AP]`
cited the current DCAT-AP (10 July 2025) instead of 2.0.1, and `[VOCAB-DCAT-2]`,
`[FOAF]`, `[BCP47]` and five RFCs had other dates, URLs or authors. These nine
entries are pinned in `localBiblio` with the published values.

Differences that remain:

| Published page | Build | Why |
|----------------|-------|-----|
| "as a recommendaton." | "as a Recommendation." | Typed by hand; the profile generates the sentence |
| No endorsement sentence | "Publication as a Recommendation does not imply endorsement by the European Commission." | Deleted by hand; the profile writes it for `specStatus: "RE"`. Removing it would need a change to the profile or to `dist/index.html` after rendering |
| `NAPCORE <time>Recommendation 17 January 2025</time>` | `NAPCORE Recommendation <time>17 January 2025</time>` | Markup only |
| Empty `<dd>` after "Reviewed by" and "Approved by" | None | Leftovers of the hand edit |

Whitespace and markup details also differ: the published page was saved from
a browser, the build is written by the ReSpec CLI.

## Ontology source

1.1.0 was set up with the RDF/XML, a Protégé export, as the source: a script
generated the Turtle and the JSON-LD from it with `rdfpipe`. In practice the
three files were edited by hand in parallel and drifted apart. At the release
(`33521d2`) the Turtle and the RDF/XML differed by 73 and 77 triples and the
JSON-LD was not valid JSON. At `fc6cb37` the texts are the same, but the Turtle
has `rdf:type rdf:Property` on 35 properties where the RDF/XML and the JSON-LD
have OWL declarations on 33 terms, the RDF/XML alone has the `rdfs:comment` of
`dcat:temporalResolution`, and the JSON-LD has CRLF line breaks in 38
multi-line comments.

The conversion first made the Turtle the source, as on `main`, then returned
to the RDF/XML:

- `src/mobilitydcat-ap.rdf` is the file at `fc6cb37`, published unchanged by
  the build, with two edits: the `dcat:temporalResolution` comment is removed,
  completing `8398ce7`, which removed the property from the other two files;
  and the 35 `rdf:Property` types of the Turtle are added, one line per
  property as the first child of its element. It now holds every triple of the
  old Turtle plus the 33 OWL declarations.
- `serialise.py` generates the Turtle, JSON-LD and N-Triples from it with
  rdflib, using the prefixes of the RDF/XML (`mobilitydcatap:`, `dct:`, ...).

## Verification

- `mise run lint`: no broken local references; 211 `html-validate` errors, the
  baseline (161 trailing whitespace from the ReSpec CLI; the
  `prefer-native-element`, `wcag/h63` and `parser-error` errors are on the
  published page too, its `close-order` and `no-implicit-close` errors are
  gone).
- Every file under `releases/1.1.0/` and `releases/latest/` on `gh-pages` is in
  `dist/`.
- The generated `.ttl`, `.jsonld` and `.nt` are isomorphic to
  `src/mobilitydcat-ap.rdf` and byte-identical between builds.
- `build-check.yml` succeeds on GitHub.
- Compared with `releases/index.html`: the same visible text apart from the
  differences that remain above, the same links, and the same bibliography
  (77 entries, 288 citations).

## What the first publish changes on `gh-pages`

A push to `release/1.1.0` replaces `releases/1.1.0/`, and `releases/latest/`
(a copy of the root of `releases/`) while `LATEST_RELEASE` on `main` reads
`1.1.0`:

- `index.html`: the status paragraph. `releases/1.1.0/index.html` also gets
  the hand edits it lacked (`faf4ed9`, #164, `c690a85`, `8b0c12e`).
- `releases/1.1.0/` gets `figures/`, so its UML diagrams load again, the
  Enterprise Architect documentation page, and the root copies of the
  Enterprise Architect `readme.md` and `.qea`.
- `shaclShapes/README.md` is the source copy, without the links added on
  `gh-pages` (`3ebb191`, `41ca6cc`).
- `mobilitydcat-ap.rdf` gains the 35 `rdf:Property` types and loses the
  `dcat:temporalResolution` comment. The generated `.ttl` has every published
  triple plus the 33 OWL declarations; the `.jsonld` gains the 35 types and LF
  line breaks in the 38 comments. The `.nt` is new.

The root of `releases/` is not touched, so w3id.org's `/releases/` and
`/releases/latest/` keep serving the hand-edited page and the old files.

## Open points

- `publishDate` is still 2025-01-17; the hotfix procedure on `main` sets it to
  the date of the correction.
- `src/shaclShapes/README.md` differs from both published copies, which also
  differ from each other.
- `releases/` and `drafts/` are still on the branch, as copies of what was
  published by hand; nothing is built or published from them.
- `REPOSITORY.md` on `main` still says that `release/1.1.0` has no build.
- Broken links, on the published page too: Annex H.1 links
  `./mobilitydcat-ap_shacl_shapes.ttl`, which was never published next to the
  page; the Enterprise Architect documentation page links
  `../1.1.0/validationFiles/`, renamed `shaclShapes/` in `1277397`.
- `src/catalog-v001.xml` maps the ontology to `mobilitydcatap.rdf`, a file name
  from before 1.1.0.
- The 1.1.0 examples are not validated against the SHACL shapes;
  `validate-examples.py` would have to be adapted.
