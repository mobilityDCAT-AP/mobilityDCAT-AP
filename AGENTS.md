# Agent instructions

Guidance for coding agents working on this branch. `CLAUDE.md` imports this
file rather than restating it.

This is `release/1.1.0`: the sources of the published mobilityDCAT-AP 1.1.0,
built with the tooling of `main`. The working draft of the next version is on
`main`, whose `AGENTS.md` describes the project and its documents.
`DEVELOPMENT.md` here describes how this branch differs from `main`.

## Hard rules

**A push to `release/1.1.0` publishes.** It replaces `releases/1.1.0/` on
`gh-pages`, and `releases/latest/` as well while `LATEST_RELEASE` on `main`
reads `1.1.0`. Work on another branch and open a pull request against
`release/1.1.0` unless told otherwise.

**Never edit `dist/`.** It is regenerated on every build.

**Never commit generated RDF.** The ontology is edited in RDF/XML,
`src/mobilitydcat-ap.rdf`, as 1.1.0 always was (unlike `main`, where Turtle is
the source); its Turtle, JSON-LD and N-Triples are generated. The examples in
`src/examples/` are the exception: their Turtle and RDF/XML are both
maintained by hand.

**Keep the release values in `src/config.js`.** `specStatus: "RE"` and the
`releases/1.1.0/` URLs are what the published page shows.

**Do not change `src/js/respec-napcore.js`** beyond what its header comment
describes; it is a copy of the NAPCORE ReSpec profile.

## Verifying a change

```sh
mise run lint
```

It should report no broken local references, and 211 `html-validate` errors,
which are a baseline from the ReSpec markup.

## Conventions

As on `main`: commit subjects start with `Dev:`, `CI:` or `Docs:`, messages are
short and wrapped at 72 characters, text files use LF, and build scripts are
Python that runs on Windows and Linux.
