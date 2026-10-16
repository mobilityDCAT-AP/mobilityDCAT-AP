# Development guide: release 1.1.0

This branch, `release/1.1.0`, holds the sources of mobilityDCAT-AP 1.1.0 and
publishes them to `releases/1.1.0/` on `gh-pages`. It uses the build tooling of
`main`, adapted to the 1.1.0 sources. This guide covers what differs from
`main`; for everything else, the documents on `main` apply:

| Question | Document on `main` |
|----------|--------------------|
| Installing mise, Node.js, uv and the dependencies | `DEVELOPMENT.md` |
| Which workflow publishes where, the branch naming convention | `REPOSITORY.md` |
| How to hotfix a published release | `PROCEDURES.md`, section "Hotfix a published release" |

## Build

```sh
mise trust            # once per clone
mise install          # Node 24 and uv
mise run install      # npm install + uv sync
mise run lint         # full build into dist/, then the checks
```

The tasks are the ones on `main`: `clean`, `serialise`, `build-spec`, `build`,
`mark-draft`, `validate`, `check`, `lint`, `serve` and `serve-dist`.
`validate-examples` is not available here; see below.

`mise run check` should report **no broken local references**. `html-validate`
reports **211 errors** on an unmodified tree, from the markup ReSpec 25
generates (most are trailing whitespace); the number is a baseline, not a
defect list.

The build fetches references from api.specref.org. Without network access a
local build still succeeds, with an error for every reference it could not look
up. In CI (the `CI` environment variable is set) `build-spec.py` passes
`--haltonerror`, so any ReSpec error fails the build.

## How it differs from `main`

| | `main` (3.0.0 draft) | `release/1.1.0` |
|-|----------------------|-----------------|
| ReSpec profile | stock `respec-w3c` from w3.org, replaced at build time by the version pinned in `package.json` (`--use-local`) | the NAPCORE profile (ReSpec 25.16.5), kept in the repository as `src/js/respec-napcore.js` |
| Serialised to RDF/XML, JSON-LD, N-Triples | ontology, examples, SHACL shapes | ontology only; the examples (Turtle and RDF/XML) and the SHACL shapes (Turtle) are published as they are |
| SHACL directory | `src/shacl/` | `src/shaclShapes/`, the name 1.1.0 was published with |
| `validate-examples` | yes | no: the script is written for the 3.0.0 shapes, which import DCAT-AP 3.0.1; the 1.1.0 shapes import DCAT-AP 2.0.1 |

### The NAPCORE profile

`src/index.html` loads `./js/respec-napcore.js`, a copy of
`respec-napcore.js` from
[mobilityDCAT-AP/respec-style](https://github.com/mobilityDCAT-AP/respec-style)
(last changed upstream in 2023). The copy has two changes, described at the top
of the file. It adds the label "Recommendation" for `specStatus: "RE"`. Upstream
has the stylesheet for that status, `NAPCORE-RE.css`, but no label, so the
header would read just "NAPCORE". And it looks up references at
api.specref.org: upstream uses specref.herokuapp.com, which no longer answers,
so every reference in the bibliography would read "Reference not found."

The stylesheets are still loaded from `mobilitydcat-ap.github.io` when the page
is viewed, as the W3C stylesheets are on `main`.

`mise run serve` shows the same rendering as the build, since both use this
copy.

## Publishing

Every push to `release/1.1.0` runs `build-release.yml`, which builds the branch
and replaces `releases/1.1.0/` on `gh-pages` with the result. While
`LATEST_RELEASE` on `main` reads `1.1.0`, it replaces `releases/latest/` as
well. A pull request against `release/1.1.0` is built by `build-check.yml`
without publishing.

To correct 1.1.0, follow "Hotfix a published release" in `PROCEDURES.md` on
`main`, with `release/1.1.0` as the release branch: the fix and the new
`publishDate` in `src/config.js` as separate commits. Bring the fix to `main`
only if the 3.0.0 draft has the same defect; its text has moved on from 1.1.0.

The files in the root of `releases/` on `gh-pages` are not built from here and
stay as they are. w3id.org still redirects `/releases/` and `/releases/latest/`
to them; only `/releases/1.1.0/` leads to what this branch publishes.

## Source layout

| Path | Purpose |
|------|---------|
| `src/index.html` | ReSpec specification document |
| `src/config.js` | ReSpec configuration, with the release values of 1.1.0 |
| `src/mobilitydcat-ap.ttl` | Ontology, the source of its RDF/XML, JSON-LD and N-Triples |
| `src/tables/` | HTML tables included by `index.html` |
| `src/examples/` | Examples, Turtle and RDF/XML, both maintained by hand |
| `src/shaclShapes/` | SHACL shapes |
| `src/figures/` | UML diagrams and the figures used by the wiki |
| `src/enterpriseArchitectFiles/` | Enterprise Architect model and its documentation page |
| `src/js/respec-napcore.js` | The NAPCORE ReSpec profile; `script.js` next to it is unused |
| `src/catalog-v001.xml` | Protégé import catalog; not published |
| `src/appendices/` | Empty and unused |
| `src/scripts/` | Build scripts (Python) |
