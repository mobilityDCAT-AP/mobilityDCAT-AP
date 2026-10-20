# Procedures

How to do the recurring things in this repository: edit the draft, publish a
draft snapshot for review, cut a release, promote it, and hotfix it.

The three documents divide as follows:

| Document | Answers |
|----------|---------|
| `REPOSITORY.md` | What is in the repository, the naming convention, which workflow publishes where, and a one-paragraph summary of each procedure |
| `DEVELOPMENT.md` | How to install the toolchain and build locally |
| `PROCEDURES.md` (this file) | How do I do X, step by step |

Each procedure below states when it applies, the steps, and what lands where on
the `gh-pages` branch. The refs used are the ones defined in the branching table
in [`REPOSITORY.md`](REPOSITORY.md#branching-and-naming-convention):

| Ref | Kind | Publishes to |
|-----|------|--------------|
| `main` | branch | `drafts/latest/` |
| `draft/X.Y.Z-draft.N[.C]` | tag | `drafts/X.Y.Z-draft.N[.C]/` |
| `release/X.Y.Z` | branch | `releases/X.Y.Z/`, and `releases/latest/` if it is the latest |

Everything published lives on the `gh-pages` branch and is served by GitHub
Pages, at `https://w3id.org/mobilitydcat-ap/`, which redirects to
`https://mobilitydcat-ap.github.io/mobilityDCAT-AP/`.

These procedures cover the versions built here. Releases 1.0.0, 1.0.1 and
1.1.0 were published by hand before this layout and are corrected by hand on
`gh-pages`; see `REPOSITORY.md`, section
[Versions published before this layout](REPOSITORY.md#versions-published-before-this-layout).

Steps done in the GitHub web interface also show the matching
[GitHub CLI](https://cli.github.com/) command (`gh`), for those who prefer the
terminal. `gh` must be logged in (`gh auth login`) and run inside the
repository clone.

---

## Edit the current draft

**When:** any change to the specification that is not yet a release. This is the
normal, everyday case.

**Steps**

1. Branch from `main`. Any name that is not `main`, `release/*` or `gh-pages`
   works; something like `fix/distribution-table` keeps the intent visible.

   ```sh
   git switch main
   git pull
   git switch -c fix/distribution-table
   ```

2. Edit under `src/`, and build locally before pushing:

   ```sh
   mise run lint      # full build, then HTML and reference checks
   ```

   See `DEVELOPMENT.md` for the individual steps; without a local
   toolchain, see its section
   [Without a local toolchain](DEVELOPMENT.md#without-a-local-toolchain).

3. Push the branch. `build-check.yml` runs the full build pipeline and
   **publishes nothing**. The built `dist/` is uploaded as a run artifact named
   `spec-dist`, so the rendered page can be reviewed: open the run in the
   Actions tab and download it from the Artifacts section of the run page.

   ```sh
   git push -u origin fix/distribution-table
   ```

   With `gh`, find the run, follow it and download the artifact:

   ```sh
   gh run list --branch fix/distribution-table   # run IDs
   gh run watch <run-id>
   gh run download <run-id> -n spec-dist -D spec-dist
   ```

4. Open a pull request against `main`. `build-check.yml` runs again for the pull
   request. While the pull request is open, each push to its branch builds
   twice, once for the push and once for the pull request; both runs complete,
   and both appear among the pull request's checks.

   From a fork, `gh pr create` targets the upstream repository by default. Pass
   `--repo` and `--base` to choose another one, or pick the base repository in
   the web form.

5. Merge. `build-main.yml` then builds `main` and publishes it to
   `drafts/latest/`, replacing what was there.

**Result on `gh-pages`:** `drafts/latest/` is refreshed. Nothing else moves.

**Note:** `build-main.yml` and `build-check.yml` are path-filtered to what can
change the build: `src/**`, the dependency files (`package.json`,
`package-lock.json`, `pyproject.toml`, `uv.lock`), `.python-version`,
`.mise.toml`, which holds the tool versions and the tasks CI runs, and their
own workflow files. A pull
request that only touches documentation does not trigger a build, which is
expected; `drafts/latest/` is unaffected by it either way.

---

## Publish a named draft snapshot for review

**When:** a version of the draft has to stay reachable at a stable URL, for
example to send to reviewers or to reference from a meeting agenda.
`drafts/latest/` is not suitable for that, because the next merge to `main`
overwrites it.

**Steps**

1. Decide the tag: `draft/X.Y.Z-draft.N`, where `X.Y.Z` is the version the draft
   is working towards and `N` is the review round, counting from 1. The first
   review round of the 3.0.0 draft is `draft/3.0.0-draft.1`, the second is
   `draft/3.0.0-draft.2`.

   `N` may carry an optional second number for a correction inside the same
   round: `draft/3.0.0-draft.1.1`. It sorts after `3.0.0-draft.1` and before
   `3.0.0-draft.2`. Use it when a snapshot has already gone out and needs a fix
   that does not amount to a new review round; otherwise use the plain
   `draft.N`.

2. Tag the current `main` and push the tag. `src/config.js` is not changed for
   a snapshot: it publishes with the same draft values as `drafts/latest/`.

   ```sh
   git switch main
   git pull
   mise run lint
   git tag -a draft/3.0.0-draft.1 -m "3.0.0 draft, review round 1"
   git push origin draft/3.0.0-draft.1
   ```

3. `build-draft.yml` extracts the version by stripping the `draft/` prefix,
   validates it against `^[0-9]+\.[0-9]+\.[0-9]+-draft\.[0-9]+(\.[0-9]+)?$`,
   builds, and publishes. Follow the run in the Actions tab, or with
   `gh run watch`.

**Result on `gh-pages`:** `drafts/3.0.0-draft.1/`. `drafts/latest/` is untouched;
it stays managed by `build-main.yml`.

**The snapshot's header still describes `drafts/latest/`.** Because
`config.js` is not changed, "This version" and the canonical link on the
snapshot page point at `drafts/latest/`, not at the snapshot. The text is
frozen; only those self-links are generic. When sending a snapshot out, give
its own URL, `drafts/3.0.0-draft.1/`, rather than the link in its header.
Giving each snapshot its own header would need CI to write those values; see
[What CI could fill in, and what it cannot](#what-ci-could-fill-in-and-what-it-cannot).

**Treat the snapshot as permanent.** No push re-triggers `build-draft.yml` for
an existing tag, so the published folder keeps showing the state of the source
at the moment the tag was pushed. The one way to rebuild it is a manual run of
`build-draft.yml` from that tag
(`gh workflow run build-draft.yml --ref draft/3.0.0-draft.1`), which overwrites
the folder. The result can differ from what reviewers saw if anything the build
fetches has changed since, so do not do it to a snapshot that has gone out. If a snapshot turns out to be
wrong, publish a new tag rather than moving or rebuilding the existing one:
`-draft.N.C` if it is a correction within the round, `-draft.N+1` if it is the
next round.

---

## Create a release

**When:** a version of the specification is final and should be published under
`releases/`.

**Steps**

1. Make sure every change meant for the release is merged to `main`, then
   create the release branch from it locally. Do not push it yet: the first
   push publishes.

   ```sh
   git switch main
   git pull
   git switch -c release/3.0.0
   ```

2. On the release branch, set the release values in `src/config.js` (checklist
   below) and commit them. Do not merge this change to `main`: a merge to
   `main` publishes `drafts/latest/`, and the draft must keep its draft values.
   The release branch and `main` therefore differ in `config.js` from the
   start, which is intended.

3. Build locally, then push the branch:

   ```sh
   mise run lint
   git push -u origin release/3.0.0
   ```

   To have the release values reviewed before they are published, push the
   same commit to a branch with another name first, for example
   `git push origin release/3.0.0:prepare/3.0.0`. `build-check.yml` builds it
   without publishing, and the built `dist/` is attached to the run. Delete
   that branch once the release branch is pushed:
   `git push origin --delete prepare/3.0.0`.

4. `build-release.yml` extracts the version from the branch name, validates it
   against `^[0-9]+\.[0-9]+\.[0-9]+$` (no pre-release suffix is accepted on a
   release branch), builds, and publishes. Follow the run in the Actions tab,
   or with `gh run watch`.

5. The same workflow reads `LATEST_RELEASE` from `main` with a sparse checkout
   and compares it to the branch version. If they match, a second `publish-latest`
   job also deploys to `releases/latest/`. For a brand new version they will
   not match yet; promote it as in
   [Promote a release to latest](#promote-a-release-to-latest).

6. Move the draft on `main` past the release. From now on `main` works towards
   the next version, and its `config.js` still names the release before this
   one. Change it through a pull request, as in
   [Edit the current draft](#edit-the-current-draft):

   - "Document version": the next version, once the editors have decided it;
   - `prevVersionURI` and "Previous version:": the release just published;
   - `prevRecURI`: the release just published, if it counts as formally
     published.

   This applies to a release cut from `main`. For a release branched from an
   older release branch (see
   [Hotfix a published release](#hotfix-a-published-release)), the editors
   decide whether the draft should name it.

**Result on `gh-pages`:** `releases/3.0.0/`, and `releases/latest/` as well if
`LATEST_RELEASE` on `main` already reads `3.0.0`.

**The release branch is long-lived.** It stays in the repository so hotfixes can
be made on it (see [Hotfix a published release](#hotfix-a-published-release)).
Do not delete it after publishing.

### `config.js` checklist: draft vs release

All of these live in `src/config.js`; search for the field name or the
`otherLinks` key, since line numbers move with every change. The
mistake this checklist exists to prevent is a mix of draft and release values:
for example `specStatus: "unofficial"` and `canonicalURI` pointing at
`drafts/latest/`, next to a `thisVersionURI` pointing at `releases/3.0.0/`.
Check the whole table each time, not only the fields you came to change.

| Field | Draft (`main`, and every `draft/*` snapshot taken from it) | Release (`release/X.Y.Z`) |
|-------|---------------------------|---------------------------|
| `publishDate` | omitted, so ReSpec shows the build date | the release date |
| `specStatus` | `"unofficial"` | the agreed published status (see [ReSpec specStatus](https://respec.org/docs/#specStatus)) |
| `latestVersion` | `https://w3id.org/mobilitydcat-ap/releases/` | unchanged |
| `canonicalURI` | `.../drafts/latest/` | `.../releases/X.Y.Z/` |
| `prevRecURI` | the last formally published release | the last formally published release |
| `thisVersionURI` | `.../drafts/latest/`, matching `canonicalURI` | `.../releases/X.Y.Z/` |
| `prevVersionURI` | the release this draft supersedes | the release this one supersedes |
| `latestVersionURI` | `https://w3id.org/mobilitydcat-ap/releases/` | unchanged |
| `edDraftURI` | `.../drafts/latest/` | `.../drafts/latest/` (the editor's draft is always `main`) |

Four more entries are easy to miss, because they are hard-coded `otherLinks`
rows rather than ReSpec fields. Three carry version numbers by hand; for the
two link rows, set `value` and `href` to the same URL:

| Entry | Draft (`main`) | Release (`release/X.Y.Z`) |
|-------|----------------|---------------------------|
| `otherLinks` → "Document status" | a draft status, for example "Draft"; never "Completed" | "Completed" |
| `otherLinks` → "Document version" | the version the draft is working towards | the version number being published |
| `otherLinks` → "Previous version:" | the release this draft supersedes | the release this one supersedes |
| `otherLinks` → "This version:" | `.../drafts/latest/` | `.../releases/X.Y.Z/` |

Note that the `otherLinks` rows use `https://mobilitydcat-ap.github.io/mobilityDCAT-AP/...`
while the ReSpec fields above use `https://w3id.org/mobilitydcat-ap/...`. The two
forms resolve to the same pages; keeping each entry consistent with its
neighbours matters more than unifying them.

Do not fix any of this by editing the built HTML in `dist/`. The next automated
build overwrites `dist/` entirely. Anything that cannot be expressed in
`config.js` belongs in `src/index.html`.

### The draft notice

Whatever the header says, CI marks every build except a release as a draft. A
notice at the top of the page says what the build is (the working draft, a
draft snapshot such as `3.0.0-draft.1`, or an unpublished build of a branch or
pull request), the commit and the build date, that it is not a release, and
that the header describes the release the draft prepares. It links to the
current release. A "Draft" badge stays in the corner while scrolling, and the
page title starts with "Draft: ".

`src/scripts/mark-draft.py` adds all three to `dist/index.html` after the
ReSpec build. Nothing in `config.js` controls it, and a release build never
gets it, so the release procedure has no step for it. It does not replace this
checklist: the header under the notice still shows the values above.

### What CI could fill in, and what it cannot

Four of the fields above are a pure function of the ref that triggered the build,
and a workflow step could write them into `config.js` before the ReSpec build.
For a draft snapshot, which publishes `main`'s values unchanged, this is the
only way it could get a header naming its own URL:

- `thisVersionURI` and `canonicalURI` — derivable from the branch or tag name,
  which the `extract-version` job already parses.
- `publishDate` — the build date.
- `specStatus` — determined by which workflow is running.

Two cannot be derived and need a human decision:

- `prevVersionURI` — which release this one supersedes.
- `prevRecURI` — which release counts as the last formally published one.

Whether to automate the first group is undecided and not implemented here. The
trade-off: it removes four manual steps from this
checklist, but it makes a local build and a CI build produce different metadata
from the same source, which is a real cost when debugging a published page.

---

## Promote a release to latest

**When:** a published release should become the one in `releases/latest/`,
which `https://w3id.org/mobilitydcat-ap/releases/` points at. This is always a
deliberate step; no version becomes latest on its own.

**Steps**

1. Confirm `releases/X.Y.Z/` already exists on `gh-pages`. `promote-latest.yml`
   copies what is published; it does not build. It checks this itself before
   changing anything, and rejects a version that is not `X.Y.Z`, so a mistake
   leaves both `main` and `gh-pages` untouched.

   ```sh
   git fetch origin
   git ls-tree -d --name-only origin/gh-pages releases/3.0.0   # prints the path if it exists
   ```

2. Actions tab → **Promote release to releases/latest** → Run workflow →
   enter the version, for example `3.0.0`. With `gh`:

   ```sh
   gh workflow run promote-latest.yml --ref main -f version=3.0.0
   gh run watch          # pick the promote run
   ```

3. The workflow does two things:
   - writes the version into `LATEST_RELEASE` on `main` and commits it;
   - replaces `releases/latest/` on `gh-pages` with a copy of
     `releases/X.Y.Z/` directly.

4. Confirm both landed, because they are two separate commits on two branches:

   ```sh
   git fetch origin
   git show origin/main:LATEST_RELEASE          # must read X.Y.Z
   git log -1 --oneline origin/gh-pages         # promote commit for releases/latest
   ```

   Then open `releases/latest/` on the published site and check the version shown on
   the page.

**Result on `gh-pages`:** `releases/latest/` is a copy of `releases/X.Y.Z/`.
On `main`, `LATEST_RELEASE` now reads `X.Y.Z`.

**Why `LATEST_RELEASE` matters afterwards.** It is the marker
`build-release.yml` checks on every push to a `release/*` branch. Once it reads
`3.0.0`, any later hotfix pushed to `release/3.0.0` refreshes both
`releases/3.0.0/` and `releases/latest/` in the same run, with no second manual
step. Before promotion, a push to that branch would only refresh the versioned
directory.

`LATEST_RELEASE` lives on `main` only. Release branches never carry it, so a
hotfix branch cannot accidentally promote itself.

---

## Hotfix a published release

**When:** a correction has to reach an already published release without waiting
for the next version.

A hotfix rewrites `releases/3.0.0/` in place and keeps the version number. Use
it for corrections that do not change what the release specifies, such as a
typo or a broken link. A change that warrants a new version number is a new
release instead: branch `release/3.0.1` from `origin/release/3.0.0`, not from
`main`, and continue with step 2 of [Create a release](#create-a-release).
`releases/3.0.0/` then stays as it was published.

There are two ways to do a hotfix. Pushing straight to the release branch is quicker
but publishes without review; going through a pull request adds a review and a
build check before anything is published. Both end with the same result.

**Result on `gh-pages`:** `releases/3.0.0/` is rebuilt. If `LATEST_RELEASE` on
`main` reads `3.0.0`, `releases/latest/` is rebuilt in the same run. Bringing
the fix to `main` refreshes `drafts/latest/` when it is merged.

**A hotfix to a branch that is not the latest leaves `releases/latest/`
untouched.** That is the intended behaviour: correcting an old release must not
change what current readers see. If the fix does belong in the latest release
too, apply it to that branch as well, the same way.

### Hotfix without a pull request

**When:** the fix is small and urgent, such as a broken link or a typo, and
someone with push access to the release branch takes responsibility for it.
Nobody reviews the change before it is live, and CI does not stop a publish
when a check fails (see [Where things end up](#where-things-end-up)), so the
local `mise run lint` is what catches a mistake. If `release/*` is protected against direct pushes, the push is rejected;
use [Hotfix with a pull request](#hotfix-with-a-pull-request) instead.

**Steps**

1. Switch to the release branch and bring it up to date. `git switch` creates
   the local branch from `origin/release/3.0.0` if it does not exist yet:

   ```sh
   git fetch origin
   git switch release/3.0.0
   git pull --ff-only
   ```

2. Make the fix under `src/` and commit it on its own, without the `config.js`
   change from the next step. A separate commit is what lets the fix be
   cherry-picked to `main` later without the release metadata.

3. Set `publishDate` in `src/config.js` to the date of the hotfix and commit it
   separately. Nothing else in the
   [`config.js` checklist](#configjs-checklist-draft-vs-release) changes: the
   page stays at `releases/3.0.0/` under the same version number, so the
   version, `thisVersionURI`, `canonicalURI` and the `otherLinks` rows stay as
   they are.

4. Build locally, then push. The push triggers `build-release.yml`, which
   builds `release/3.0.0` and publishes it, exactly as it does for a new release
   branch:

   ```sh
   mise run lint
   git push
   ```

5. If the defect is also in the current draft, which it usually is, bring the
   fix to `main` as in [Edit the current draft](#edit-the-current-draft),
   cherry-picking only the fix commit from step 2. It goes through a pull
   request there, so the draft still gets a review:

   ```sh
   git switch main
   git pull
   git switch -c fix/typo-from-3.0.0
   git cherry-pick <fix-commit>
   ```

   Skipping this step means the next release ships the defect again.

### Hotfix with a pull request

**When:** the fix needs a second pair of eyes, is more than a trivial
correction, or `release/*` is protected against direct pushes.

**Steps**

1. Branch from the release branch, not from `main`. Fetch first, so the release
   branch is there even if it was created after the last fetch:

   ```sh
   git fetch origin
   git switch -c fix/3.0.0-typo origin/release/3.0.0
   ```

   Any name that is not `main`, `release/*` or `gh-pages` works, as in
   [Edit the current draft](#edit-the-current-draft).

2. Commit the fix and the `publishDate` change as two separate commits, as in
   steps 2 and 3 of
   [Hotfix without a pull request](#hotfix-without-a-pull-request).

3. Build locally, push the branch, and open a pull request against
   `release/3.0.0`, not against `main`:

   ```sh
   mise run lint
   git push -u origin fix/3.0.0-typo
   ```

   `build-check.yml` builds the pull request and publishes nothing; the built
   `dist/` is attached to the run for review. As in
   [Edit the current draft](#edit-the-current-draft), the run for the branch
   push appears among the pull request's checks as well.

   With `gh`, set the base explicitly; from a fork, add `--repo` as well:

   ```sh
   gh pr create --base release/3.0.0
   ```

4. Merge with a merge commit or by rebasing, not by squashing. A squash merge
   turns the fix and the `publishDate` change into one commit, and step 5
   then cannot take the fix without the release metadata. With `gh`:
   `gh pr merge --merge`. `build-release.yml` then builds `release/3.0.0` and
   publishes it.

5. Bring the fix commit to `main`, as in step 5 of
   [Hotfix without a pull request](#hotfix-without-a-pull-request).

---

## Where things end up

| Ref you push | Workflow | `gh-pages` directory |
|--------------|----------|----------------------|
| any other branch, or a PR | `build-check.yml` | nothing; `dist/` as a run artifact |
| `main` | `build-main.yml` | `drafts/latest/` |
| `draft/X.Y.Z-draft.N[.C]` tag | `build-draft.yml` | `drafts/X.Y.Z-draft.N[.C]/` |
| `release/X.Y.Z` branch | `build-release.yml` | `releases/X.Y.Z/`, plus `releases/latest/` if marked |
| (manual run) | `promote-latest.yml` | `releases/latest/`, and `LATEST_RELEASE` on `main` |

The four workflows that build (`build-check.yml`, `build-main.yml`,
`build-draft.yml` and `build-release.yml`) share the same build through
`reusable-build.yml`. The three of them that publish deploy through
`reusable-publish-gh-pages.yml`, which pre-cleans the target directory before
writing, so a published directory never keeps a file that has been removed
from the source. `promote-latest.yml` builds nothing; it replaces
`releases/latest/` with a copy of an already published `releases/X.Y.Z/`.

The checks are reported, not enforced. A failed build stops a publish, but a
failed `mise run check` (invalid markup or a broken reference)
only shows as a failed step in the run log; the run still succeeds and
publishes. Run `mise run lint` locally before pushing anything that publishes,
and look at the check step of the run afterwards. This applies to every procedure above, including a
merged pull request.
