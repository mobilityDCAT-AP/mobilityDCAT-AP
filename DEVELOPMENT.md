# Development guide

This guide covers the toolchain: prerequisites, setup, building and linting
locally. For the editing and publishing procedures that use it - edit the draft,
tag a draft snapshot, create a release, promote it, hotfix it - see
[`PROCEDURES.md`](PROCEDURES.md).

## Prerequisites

- [git](https://git-scm.com/)
- [mise](https://mise.jdx.dev/) — manages Node.js and uv versions locally
- optional: the [GitHub CLI](https://cli.github.com/) `gh`, used in some
  commands in `PROCEDURES.md`; the same can be done on the GitHub website

All build scripts are written in Python and work identically on Windows and Linux. No bash required on either platform.

No administrator rights are needed: mise, the tools it installs and every
dependency go into the user's home directory or the clone. The setup does
download programs, though, which some organisations block. What it fetches,
and from where:

| What | Fetched by | From |
|------|-----------|------|
| mise | winget, scoop or `curl https://mise.run \| sh` | github.com, mise.run |
| Node.js 24, uv | `mise install` | nodejs.org, github.com |
| Python 3.12, if not installed already | uv, on the first `uv sync` | github.com |
| Python packages (rdflib, pyshacl, ...) | `uv sync` | pypi.org, files.pythonhosted.org |
| npm packages (respec, puppeteer, ...) | `npm install` | registry.npmjs.org |
| Chrome for Testing and Chrome Headless Shell, several hundred MB, into `~/.cache/puppeteer/` | puppeteer, during `npm install` | storage.googleapis.com |

The build itself needs network access too: ReSpec looks up the references
that `src/config.js` does not define itself (for example BCP47) at
api.specref.org. `mise run validate-examples` downloads the vocabularies the
SHACL shapes import (publications.europa.eu, w3.org, semiceu.github.io and
others) once, into `.cache/shacl/`.

### Installing mise

**Linux / macOS**
```sh
curl https://mise.run | sh
```

**Windows** (PowerShell or cmd)
```powershell
winget install jdx.mise
# or
scoop install mise
```

### Without a local toolchain

Changes can also be made entirely on the GitHub website: edit the files under
`src/` in a new branch and open a pull request, as in `PROCEDURES.md`, section
[Edit the current draft](PROCEDURES.md#edit-the-current-draft).
`build-check.yml` then builds the branch and attaches the rendered `dist/` to
the run as the artifact `spec-dist`. It runs the same checks as
`mise run lint`, but a failed check does not fail the run, so read the check
step in the run log.

## First-time setup

```sh
mise trust            # once per clone: .mise.toml sets environment variables, so mise asks first
mise install          # installs Node 24 and uv (uv installs Python 3.12, from .python-version, automatically)
mise run install      # npm install + uv sync (creates .venv with all Python dependencies)
```

## Build

```sh
mise run build        # full build: serialise Turtle + build ReSpec spec
```

All output is written to **`dist/`**. Open `dist/index.html` in a browser to preview the built specification.

ReSpec prints `[ERROR] Network error loading highlighter` during the build. It
is harmless: the highlighter colours code blocks, and the specification has
none. The build still succeeds.

Individual steps:

```sh
mise run clean        # empty dist/ (run automatically at the start of mise run build)
mise run serialise    # convert src/*.ttl, src/examples/*.ttl and src/shacl/*.ttl -> .rdf + .jsonld in dist/
mise run build-spec   # copy assets to dist/ and build dist/index.html via ReSpec
```

CI also marks every build except a release as a draft, after `mise run build`.
To see a page as CI publishes a draft:

```sh
DRAFT_LABEL="the working draft" mise run mark-draft
```

In PowerShell, set the variable first: `$env:DRAFT_LABEL = "the working draft"`.

Without `DRAFT_LABEL` the notice calls the page "a local build of the draft".
Run it once per build; on a page that already has the notice it stops with an
error.

## Linting

```sh
mise run lint         # full build, then mise run check
mise run check        # both checks below, on an existing build
mise run validate     # HTML markup validation only (requires a prior build)
```

`mise run validate` on its own exits 1, because it reports the baseline errors
described below as a failure. Only `mise run check` ignores them.

`mise run lint` runs the full build, then `mise run check`, which:
1. Validates `dist/index.html` markup with `html-validate` (rules defined in `.htmlvalidate.json`)
2. Parses `dist/index.html` with `src/scripts/check-refs.py`, which cross-references all `id` attributes against all `href="#..."` links and prints each broken one

The SHACL validation of the examples used to be a third step. It is disabled for
now, because of issues with the validation itself; see [Validating the examples](#validating-the-examples).

ReSpec only reports a count of broken references in its CLI output — `check-refs.py` gives the actual list.

The checks run in this order and the first failure stops the task. `html-validate` never stops
it: its 1748 errors come from the ReSpec-generated markup and are a baseline,
not a failure.

## Validating the examples

```sh
mise run validate-examples                  # src/examples/*.ttl against the SHACL shapes
mise run validate-examples -- --offline     # use only the cached imports
mise run validate-examples -- path/to/file.ttl
```

The shapes are the four constraint files in `src/shacl/`. What they
`owl:import` is downloaded on the first run (about 8 MB, 20 seconds) into
`.cache/shacl/` and reused afterwards; `--refresh` downloads it again. The
controlled vocabularies from `mdr-imports.ttl` go into the data graph, because
the membership checks look them up there, and the DCAT-AP 3.0.1 base shapes go
into the shapes graph. Only results on nodes of the validated file are printed.
The task exits 1 on any `sh:Violation`; warnings are printed only.

The DCAT-AP `range.ttl` is left out unless `--with-dcat-ap-ranges` is given. Its
`sh:class` checks need an explicit type on every value, which the EU authority
tables do not carry, so on the current examples it reports every codelist value.
Validation runs without inference: RDFS inference over DCAT 2 makes every
`dcat:Catalog` a `dcat:Dataset` and applies the Dataset rules to it.

It is not part of `mise run check` for now, so it does not run in `mise run lint`
or in CI, because of issues with the validation itself. Run it on demand with
the commands above. CI still keeps `.cache/shacl/` between runs, under a key that changes each month and
whenever a file in `src/shacl/` changes.

## Live preview

To use ReSpec's interactive warnings panel in the browser:

```sh
mise run serve        # starts HTTP server on http://localhost:8080
```

Open `http://localhost:8080/src/index.html` in a browser. ReSpec runs live and shows a warnings badge at the top — click it to see all issues with locations. Stop with `Ctrl+C`.

The live preview uses the current ReSpec from w3.org, which `src/index.html`
loads, while `mise run build` uses the version pinned in `package.json`. The two
can render slightly differently; the build is what gets published.

## How it works

| Step | Script | What it does |
|------|--------|-------------|
| Serialise | `src/scripts/serialise.py` | Parses each `.ttl` with rdflib, keeping every literal as written (rdflib would otherwise rewrite typed literals such as `xsd:dateTime`), writes `.rdf` and `.jsonld` to `dist/`; writes lists of literals (`sh:languageIn`) as nested `rdf:first`/`rdf:rest`, which rdflib's pretty RDF/XML gets wrong, and falls back to flat RDF/XML if the output does not round-trip. Names blank nodes from their content, sorts the triples and fixes `PYTHONHASHSEED`, so the same Turtle always gives byte-identical files and a rebuild publishes no changes |
| Copy assets | `src/scripts/copy-assets.py` | Copies the Turtle sources, examples, figures, SHACL shapes and the migration guide to `dist/` |
| Build spec | `src/scripts/build-spec.py` | Calls `respec --localhost`, which spins up its own HTTP server, builds `dist/index.html`, and shuts down |
| Mark draft | `src/scripts/mark-draft.py` | Adds the draft notice, a "Draft" badge and a "Draft: " title prefix to `dist/index.html`; run by CI for every build except a release, not part of `mise run build` |
| Validate examples | `src/scripts/validate-examples.py` | Runs pyshacl on the examples; separate from the build |

`--localhost` is required because Chromium (used internally by ReSpec) blocks `file://` requests needed by `data-include`. All paths (`src/index.html` → `dist/index.html`) are defined in `build-spec.py`.

## Source layout

All hand-authored files live under `src/`. Never edit files in `dist/` — they are generated.

Turtle is the source format for the ontology, the examples and the SHACL shapes. The `.rdf` and `.jsonld` serialisations are generated on every build and are never committed.

| Path | Purpose |
|------|---------|
| `src/mobilitydcat-ap.ttl` | Ontology — primary source of truth (Turtle) |
| `src/index.html` | ReSpec specification document |
| `src/config.js` | ReSpec configuration (version, editors, dates, bibliography) |
| `src/tables/` | HTML property tables included by `index.html` via `data-include` |
| `src/examples/` | Worked examples (Turtle) |
| `src/shacl/` | SHACL validation constraints |
| `src/figures/` | UML diagrams |
| `src/migrationGuide/` | Migration guide from 1.1.0 (spreadsheet), linked from `index.html` |
| `src/catalog-v001.xml` | Protégé import catalog for editing the ontology; not published |
| `src/js/` | Custom JavaScript |
| `src/appendices/` | Empty and unused, left over from GeoDCAT-AP; the appendices themselves are sections of `index.html` |
| `src/scripts/` | Build scripts (Python) |

## Dependencies

| Tool | Version | Managed by | Purpose |
|------|---------|-----------|---------|
| Node.js | 24 | mise | Runtime for ReSpec |
| respec | 36.0.0 | npm / `package.json` | Builds the HTML specification |
| uv | latest | mise | Python package manager |
| Python | 3.12 | uv / `.python-version` | Runtime for build scripts |
| rdflib | 7.6.0 | uv / `pyproject.toml` | RDF serialisation |
| pyshacl | 0.31.0 | uv / `pyproject.toml` | SHACL validation of the examples |

- `.mise.toml` — pins Node and uv versions
- `.python-version` — pins the Python version uv uses, locally and in CI
- `package.json` — pins respec
- `pyproject.toml` — declares Python dependencies
- `uv.lock` — exact locked versions; commit this file for reproducible installs

## CI

Every publishing workflow builds through the reusable workflow
`.github/workflows/reusable-build.yml`, which runs the same mise tasks as
`mise run lint`, with the same tool versions from `.mise.toml`, on the
runner image `ubuntu-24.04` (pinned in every workflow, so a new image is a
change by commit, not by GitHub):
`mise run install`, `mise run build`, then `mise run check`. Between the build
and the check it runs `mise run mark-draft`, unless the calling workflow passes
no `draft_label`, which only `build-release.yml` does. The build is
enforced; `check` runs with `continue-on-error`, so a failed check shows in the
log but does not stop a publish. A new check therefore goes into the `check`
task, not into the workflow. Which ref publishes
where is listed in `REPOSITORY.md`; the step-by-step procedures are in
[`PROCEDURES.md`](PROCEDURES.md).
