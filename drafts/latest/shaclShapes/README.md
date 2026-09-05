# mobilityDCAT-AP SHACL Shapes (v3.0.0)

This directory contains the SHACL shapes for validating mobilityDCAT-AP v3.0.0 metadata. mobilityDCAT-AP v3.0.0 extends DCAT-AP 3.0.1: the constraint files import the corresponding DCAT-AP 3.0.1 file via `owl:imports` and contain only the mobilityDCAT-AP-specific additions (deltas).

## Files

- `shapes.ttl` - Core constraints (cardinality, nodeKind, datatype, pattern) for mobilityDCAT-AP classes and properties.
- `ranges.ttl` - Range constraints (`sh:class` / `sh:nodeKind`) for property values.
- `mdr-vocabularies.ttl` - Controlled-vocabulary (codelist) membership constraints.
- `deprecated-uris.ttl` - Warnings for deprecated mobilityDCAT-AP properties. DCAT-AP's own 2.x to 3.x deprecations are inherited via import, not restated here.
- `imports.ttl` - Imports the DCAT-AP 3.0.1 SHACL shapes and other base ontologies.
- `mdr-imports.ttl` - Imports the controlled-vocabulary codelists. A validator must load these for the controlled-vocabulary checks to work, since membership is evaluated against the data graph.

## Namespaces

Each shape file declares its own versioned namespace, so shapes from different files do not collide:

- `shapes.ttl` -> `https://w3id.org/mobilitydcat-ap/releases/3.0.0/shacl/shapes#`
- `ranges.ttl` -> `https://w3id.org/mobilitydcat-ap/releases/3.0.0/shacl/ranges#`
- `mdr-vocabularies.ttl` -> `https://w3id.org/mobilitydcat-ap/releases/3.0.0/shacl/mdr-vocabularies#`
- `deprecated-uris.ttl` -> `https://w3id.org/mobilitydcat-ap/releases/3.0.0/shacl/deprecated-uris#`

`imports.ttl` and `mdr-imports.ttl` declare their `owl:imports` directly on the version IRI `https://w3id.org/mobilitydcat-ap/releases/3.0.0`.

## Severity levels

- `sh:Violation` - Mandatory properties. Must be fixed.
- `sh:Warning` - Recommended and deprecated properties. Should be addressed.
- `sh:Info` - Optional properties. May be added.

Controlled-vocabulary constraints follow the categories in section 10.2 of the specification.

## Validation

For validation, see: **https://github.com/mobilityDCAT-AP/validation**

## Previous version

SHACL shapes for v1.1.0 are in `drafts/1.1.0-draft-0.1/shaclShapes`.