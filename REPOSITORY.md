# How this repository works

This document describes the source layout, the versioning convention and the
GitHub Actions publishing workflow of the
[mobilityDCAT-AP](https://w3id.org/mobilitydcat-ap/releases/) repository. What
mobilityDCAT-AP is, and where to report issues, is in [`README.md`](README.md).

# Concepts

## Sources and build output

The specification document is a [ReSpec](https://respec.org/) page,
`src/index.html`, configured by `src/config.js`. ReSpec renders it into a static
HTML page at build time.

The ontology, `src/mobilitydcat-ap.ttl`, and the worked examples in
`src/examples/` are written in Turtle, which is the source format. The RDF/XML
and JSON-LD serialisations are produced by the build and never committed.

The SHACL shapes in `src/shacl/` are the validation constraints of the
profile. They are also written in Turtle, and the build publishes them as
RDF/XML and JSON-LD the same way. `mise run validate-examples` validates the
examples against them. It is not part of `mise run check` for now, because of
issues with the validation itself.

Everything hand-authored lives in `src/`. The build writes everything it
produces to `dist/`, which is emptied at the start of each build and must not be
edited by hand.

```
src/
├── index.html                 # ReSpec specification document (entry point)
├── config.js                  # ReSpec configuration: version, editors, dates, links
├── mobilitydcat-ap.ttl        # Ontology, primary source of truth
├── tables/                    # HTML property tables included by index.html
├── examples/                  # Worked examples
├── figures/                   # UML diagrams and logo
├── shacl/                     # SHACL validation constraints
├── migrationGuide/            # Migration guide from 1.1.0 (spreadsheet)
├── js/                        # Custom JavaScript
├── scripts/                   # Build scripts (Python)
├── catalog-v001.xml           # Protégé import catalog; not published
└── appendices/                # Empty, unused; left over from GeoDCAT-AP
```

## Published versions

Every published version is a directory on the `gh-pages` branch, served by
GitHub Pages. The persistent address `https://w3id.org/mobilitydcat-ap/`
redirects to the Pages site `https://mobilitydcat-ap.github.io/mobilityDCAT-AP/`.

The editor's draft, `drafts/latest/`, is always the current `main`.

A draft snapshot, `drafts/X.Y.Z-draft.N/`, freezes the draft at a stable URL for
a review round.

Both carry a draft notice at the top of the page, added by CI, so a draft does
not pass for a release even when its header shows the values of the release it
prepares.

A release, `releases/X.Y.Z/`, is a published version of the standard. It is
built from a long-lived `release/X.Y.Z` branch, so it can be hotfixed later.

The latest release, `releases/latest/`, is a copy of one release chosen by a
person; `https://w3id.org/mobilitydcat-ap/releases/` points there. The file
`LATEST_RELEASE` on `main` records which version that is.

## Versions published before this layout

Releases 1.0.0, 1.0.1 and 1.1.0, and the drafts of those versions, were
published by hand, with the sources and the published files together on
`gh-pages`. They are not built by the workflows below.

- They stay on `gh-pages` as they are: `releases/1.0.0/`, `releases/1.0.1/`,
  `releases/1.1.0/` and `drafts/1.x.y-draft-0.1/`.
- 1.1.0 is the latest release, so `releases/latest/` holds a copy of it, and
  `LATEST_RELEASE` reads `1.1.0`. Its files also stay in the root of
  `releases/`, the earlier target of the w3id.org address.
- The branch `release/1.1.0` keeps the repository as it was when 1.1.0 was the
  current release, in the old layout. It has no build and no workflows, so a
  push to it publishes nothing. A correction to one of these versions is made
  by hand on `gh-pages`.

The first version built here replaces the 1.1.0 copy in `releases/latest/`
when it is promoted to latest. The root files are left as they are.

## Branching and naming convention

| Ref | Kind | Goes to folder in gh-pages | Example |
|-----|------|----------------------------|---------|
| `main` | branch | `drafts/latest/` | |
| `draft/X.Y.Z-draft.N[.C]` | tag | `drafts/X.Y.Z-draft.N[.C]/` | `draft/3.0.0-draft.1`, `draft/3.0.0-draft.1.1` |
| `release/X.Y.Z` | branch | `releases/X.Y.Z/`, and `releases/latest/` if it is the latest | `release/3.0.0` |

A draft snapshot is tagged `draft/X.Y.Z-draft.N`, where `X.Y.Z` is the version
the draft is working towards and `N` is the review round counting from 1. A
release is a `release/X.Y.Z` branch with no suffix. This matches how DCAT-AP
labels its own drafts by target version.

The optional `.C` in `draft.N.C` is a correction published within the same
review round, such as a typo found right after the snapshot went out. Use it
sparingly; the plain `draft.N` is the normal form.

`X.Y.Z-draft.N` is a valid SemVer pre-release, so versions order by the SemVer
rules: numeric identifiers compare as numbers, and a longer identifier list
sorts above a shorter one with the same prefix, which places a correction after
the snapshot it corrects.

```
3.0.0-draft.1  <  3.0.0-draft.1.1  <  3.0.0-draft.2  <  3.0.0-draft.10  <  3.0.0
```

CI enforces both patterns: `build-draft.yml` rejects a tag that does not match
`^[0-9]+\.[0-9]+\.[0-9]+-draft\.[0-9]+(\.[0-9]+)?$`, and `build-release.yml`
rejects a branch that does not match `^[0-9]+\.[0-9]+\.[0-9]+$`.

The older drafts on `gh-pages` use a different form, `1.1.0-draft-0.1`. They
are kept under their published names.

## mise tasks

[mise](https://mise.jdx.dev/) pins the tool versions (Node.js and uv) and
defines the build as named tasks in `.mise.toml`. CI runs the same tasks as a
local build, so the two produce the same result.

# Installation

Install [mise](https://mise.jdx.dev/getting-started.html), then in the project
folder:

```sh
mise trust          # once per clone; mise refuses an untrusted .mise.toml
mise install        # Node.js and uv at the pinned versions
mise run install    # npm install + uv sync
```

`DEVELOPMENT.md` covers installing mise on Windows and Linux.

# Configuration

A local build needs no settings, credentials or environment variables.

| What | Where |
|------|-------|
| Tool versions and task definitions | `.mise.toml` |
| ReSpec version | `package.json` |
| Python version | `.python-version` |
| Python dependencies | `pyproject.toml`, locked in `uv.lock` |
| HTML validation rules | `.htmlvalidate.json` |
| Version, dates and URLs shown in the specification | `src/config.js`; the values differ between a draft and a release, see `PROCEDURES.md`, section [`config.js` checklist: draft vs release](PROCEDURES.md#configjs-checklist-draft-vs-release) |
| Which release `releases/latest/` holds | `LATEST_RELEASE` on `main`, changed through `promote-latest.yml` |

Publishing depends on five things outside the repository files:

- GitHub Actions allowed for the repository, including the third-party
  `jdx/mise-action` next to GitHub's own `actions/checkout`, `actions/cache`,
  `actions/upload-artifact` and `actions/download-artifact`. If only GitHub's
  actions are allowed, every build fails before its first step.
- `main` as the default branch. GitHub offers a manual run only for workflows
  on the default branch, so `promote-latest.yml` and the manual runs of the
  other workflows need it.
- A `gh-pages` branch, with GitHub Pages serving from it. The publish workflow
  checks that branch out and fails if it does not exist.
- Direct pushes to `main` from GitHub Actions. `promote-latest.yml` commits
  `LATEST_RELEASE` to `main`, so a branch protection rule that blocks direct
  pushes to `main` breaks promotion.
- The `https://w3id.org/mobilitydcat-ap/` redirect, which is registered with
  the [w3id.org](https://w3id.org/) service, not configured here. It points at
  the Pages site `https://mobilitydcat-ap.github.io/mobilityDCAT-AP/`,
  and negotiates the format: a browser gets `index.html`, other clients get
  the Turtle file. Moving the published site means changing the redirect
  there.

# Usage

## Building locally

```sh
mise run build      # serialise the Turtle and build the ReSpec page into dist/
mise run lint       # build, then HTML validation and broken reference check
mise run serve      # static HTTP server on localhost:8080 for a live preview; no build
```

`mise run build` produces what CI publishes. It empties `dist/`, serialises the
Turtle ontology, examples and SHACL shapes to RDF/XML and JSON-LD, copies the
assets, and renders `src/index.html` with the ReSpec version pinned in
`package.json` into `dist/index.html`; open that file to see the result. ReSpec
prints "Network error loading highlighter" on every build; it is harmless,
because the document has no code blocks to highlight.

`mise run lint` is the check to run before pushing. It runs the build, then
`mise run check`: HTML validation of `dist/index.html` and a list of broken
local references. The first failure stops it, except the HTML validation, whose
1748 errors come from the ReSpec markup and are a baseline, not a failure.
`mise run check` alone re-runs the checks without rebuilding. The SHACL
validation of the examples is disabled for now, because of issues with the
validation itself; `mise run validate-examples` still runs it on demand.

`mise run serve` is for editing. It builds nothing; it serves the repository
files so that ReSpec can render `src/index.html` in the browser. Open
`http://localhost:8080/src/index.html` and reload after each edit; the badge at
the top lists ReSpec's warnings. The preview loads the current ReSpec from
w3.org rather than the pinned version the build uses, so it needs internet
access and can occasionally differ from the build.

The individual steps and the expected output of the checks are in
[`DEVELOPMENT.md`](DEVELOPMENT.md).

## Procedures

Every change to what is published follows one of five procedures. Each is
summarised here; the full steps, checks and edge cases are in
[`PROCEDURES.md`](PROCEDURES.md). Creating a release and hotfixing one also
involve setting the release values in `src/config.js`, following
`PROCEDURES.md`, section
[`config.js` checklist: draft vs release](PROCEDURES.md#configjs-checklist-draft-vs-release).

### Edit the current draft

For any change that is not yet a release; the everyday case. Branch from
`main`, edit under `src/`, run `mise run lint`, and open a pull request.
`build-check.yml` builds the branch without publishing it and attaches `dist/`
to the run for review. Merging to `main` refreshes `drafts/latest/`.
Full procedure: `PROCEDURES.md`, section [Edit the current draft](PROCEDURES.md#edit-the-current-draft).

### Publish a draft snapshot for review

When a version of the draft has to stay at a stable URL, for reviewers or a
meeting agenda. Tag the current `main` and push the tag; `config.js` is not
changed:

```sh
git switch main
git pull
git tag -a draft/3.0.0-draft.1 -m "3.0.0 draft, review round 1"
git push origin draft/3.0.0-draft.1
```

The snapshot keeps the draft values of `main`, so its "This version" link
points at `drafts/latest/`. Send reviewers the snapshot's own URL.

`build-draft.yml` publishes `drafts/3.0.0-draft.1/`. No later push rebuilds a
snapshot; do not move its tag or rebuild it by hand. If it is wrong, publish
`draft.1.1` or `draft.2` instead.
Full procedure: `PROCEDURES.md`, section [Publish a named draft snapshot for review](PROCEDURES.md#publish-a-named-draft-snapshot-for-review).

### Create a release

When a version is final. Create the release branch from `main`, set the
release values in `config.js` on that branch only, and push it:

```sh
git switch main
git pull
git switch -c release/3.0.0
# set the release values in src/config.js and commit
git push -u origin release/3.0.0
```

The release values never go to `main`, which keeps its draft values.

`build-release.yml` publishes `releases/3.0.0/`. The branch is long-lived and
must not be deleted, because hotfixes are made on it. Afterwards, a pull
request to `main` moves the draft past the release: the next version number and
the just-published release as the previous version.
Full procedure: `PROCEDURES.md`, section [Create a release](PROCEDURES.md#create-a-release).

### Promote a release to latest

When a published release should become the one in `releases/latest/`. This
is always a manual decision: run `promote-latest.yml` from the Actions tab with
the version number. It writes the version to `LATEST_RELEASE` on `main` and
copies the already-built `releases/X.Y.Z/` to `releases/latest/` without
rebuilding.
Full procedure: `PROCEDURES.md`, section [Promote a release to latest](PROCEDURES.md#promote-a-release-to-latest).

### Hotfix a published release

When a correction has to reach a published release before the next version.
There are two options. A small urgent fix can be committed straight to
`release/X.Y.Z` and pushed, which publishes it without review; see
`PROCEDURES.md`, section
[Hotfix without a pull request](PROCEDURES.md#hotfix-without-a-pull-request).
Otherwise, branch from `origin/release/X.Y.Z` and open a pull request against
`release/X.Y.Z`; see `PROCEDURES.md`, section
[Hotfix with a pull request](PROCEDURES.md#hotfix-with-a-pull-request).

Either way, the version number stays the same and only `publishDate` changes in
`config.js`; keep the fix in a commit separate from that change. A correction
that needs a new version number is a new release branch, such as
`release/3.0.1`, instead. Publishing rebuilds `releases/X.Y.Z/`, and also
`releases/latest/` if `LATEST_RELEASE` names that version; a hotfix to an older
release leaves `releases/latest/` alone. Cherry-pick the fix commit to `main` too, or
the next release ships the defect again.
Full procedure: `PROCEDURES.md`, section [Hotfix a published release](PROCEDURES.md#hotfix-a-published-release).

This applies to releases built here. Versions published before this layout are
corrected by hand on `gh-pages`; see
[Versions published before this layout](#versions-published-before-this-layout).

## Workflows

The procedures above trigger these workflows in `.github/workflows/`, which
build the ref and write the result to `gh-pages`.

| Workflow | Trigger | Publishes to |
|----------|---------|-------------|
| `build-main.yml` | push to `main` changing the build inputs, manual | `drafts/latest/` |
| `build-draft.yml` | push of a `draft/*` tag, manual run from that tag | `drafts/X.Y.Z-draft.N[.C]/` |
| `build-release.yml` | push to `release/*`, manual run from that branch | `releases/X.Y.Z/`, and `releases/latest/` if `LATEST_RELEASE` names this version |
| `promote-latest.yml` | manual only | sets `LATEST_RELEASE` on `main` and copies the already-built `releases/X.Y.Z/` to `releases/latest/` |
| `build-check.yml` | push to any other branch, pull request to `main` or `release/*`, manual | nothing; `dist/` is uploaded as a run artifact |

A manual run of `build-draft.yml` or `build-release.yml` takes its version from
the ref it runs on, so pick the `draft/*` tag or the `release/*` branch under
"Use workflow from" in the Actions tab, or pass it with `--ref`, as in
`gh workflow run build-release.yml --ref release/3.0.0`. Run from any other
ref, the version check fails and nothing is built.

The four workflows that build all do it through `reusable-build.yml`, which
runs `mise run build`, then `mise run mark-draft` for every build except a
release, then `mise run check`. The three that publish a build
(`build-main.yml`, `build-draft.yml` and `build-release.yml`) deploy through
`reusable-publish-gh-pages.yml`, which empties the target directory before
writing so no removed file survives. `promote-latest.yml` neither builds nor
uses that workflow: it replaces `releases/latest/` with a copy of a directory
already on `gh-pages`.

The checks are reported, not enforced. A failed build stops a publish, but a
failed `mise run check` (invalid markup or a broken reference)
only shows as a failed step in the run log; the run still succeeds and
publishes. Run `mise run lint` locally before pushing anything that publishes,
and look at the check step of the run afterwards.
