# Agent instructions

Guidance for coding agents working in this repository. Vendor-neutral by
design: `CLAUDE.md` imports this file rather than restating it.

## What this project is

**mobilityDCAT-AP** is a European standard, an RDF/OWL application profile of
DCAT-AP for describing mobility datasets, data services and services across
National Access Points in Europe. It is maintained by
[NAPCORE](https://napcore.eu/).

This repository holds the sources of the specification and the tooling that
builds and publishes them to GitHub Pages.

## Where the documentation is

This file deliberately does not repeat what the documents below say. Read the
relevant one instead of relying on a summary here; a summary is what goes
stale.

| Question | Document |
|----------|----------|
| What mobilityDCAT-AP is, where it is published, where to report issues | `README.md` |
| What is in the repository, which workflow publishes where, the branch and tag naming convention, a summary of each procedure | `REPOSITORY.md` |
| How to install the toolchain, build, lint, preview | `DEVELOPMENT.md` |
| How to edit the draft, publish a snapshot, cut a release, promote it, hotfix it, and what to set in `config.js` | `PROCEDURES.md` |

## Hard rules

**Never edit `dist/`.** It is deleted and regenerated on every build. A fix
applied there survives until the next build and no longer.

**Never commit generated RDF.** Turtle is the source format for the ontology,
the examples and the SHACL shapes. The `.rdf` and `.jsonld` serialisations are
produced by `serialise.py` into `dist/` on every build.

**Never edit `gh-pages` for a version built here.** The workflows own it. The
only hand edits there are corrections to the versions published before this
layout (1.0.0, 1.0.1, 1.1.0 and their drafts); see `REPOSITORY.md`.

**Keep the draft values in `src/config.js` on `main`.** Release values belong
on the `release/X.Y.Z` branch only; see the `config.js` checklist in
`PROCEDURES.md`. The draft notice on published drafts comes from CI
(`src/scripts/mark-draft.py`), not from `config.js`; do not add one to the
source.

## Verifying a change

```sh
mise run lint      # full build + HTML validation + broken reference check
```

Three things to know about the output, so they are not mistaken for regressions
introduced by the change at hand:

- `html-validate` reports **1748 errors** on an unmodified tree. They come from
  the ReSpec-generated markup, not from the sources. The number is a baseline to
  compare against, not a defect list to work through. If it moves, check whether
  the change at hand explains it.
- `check-refs.py` should report **no broken local references**. ReSpec prints
  only a count; this script prints the actual list.
- `validate-examples.py` is not part of `mise run lint` for now, because of
  issues with the validation itself. Run alone with `mise run validate-examples`,
  it should report **no violations**, with 4 warnings on `example-minimum.ttl`
  and 6 on `example-complete.ttl`. The warnings are known. Its first run
  downloads the SHACL imports, and a failed download of the schema.org import
  is expected.

## Conventions

- Commit subjects carry a prefix matching the history: `CI:` for workflow
  changes, `Docs:` for documentation, `Dev:` for tooling and build scripts.
  Keep messages short and wrap them at 72 characters.
- Text files use LF endings. `.gitattributes` forces `eol=lf` for `.ttl`, `.rdf`
  and `.jsonld`, because a CRLF checkout on Windows changes the content of
  multi-line RDF literals and makes a local build differ from CI.
- Build scripts are Python and must run unchanged on Windows and Linux. No bash.

## External links

- Published spec: https://w3id.org/mobilitydcat-ap/releases/
- Latest draft: https://w3id.org/mobilitydcat-ap/drafts/latest/
- Issues: https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/issues
- Namespace: `https://w3id.org/mobilitydcat-ap#`
