# mobilityDCAT-AP SHACL Shapes (v3.0.0)

This directory contains the SHACL shapes for validating mobilityDCAT-AP v3.0.0 metadata. mobilityDCAT-AP v3.0.0 extends DCAT-AP 3.0.1: each file imports the DCAT-AP 3.0.1 base via `owl:imports` and contains only the mobilityDCAT-AP-specific additions (deltas).

## Files

- `mobilitydcat-ap_3.0.0_shacl_shapes.ttl` — Core constraints (cardinality, nodeKind, datatype, pattern) for mobilityDCAT-AP classes and properties.
- `mobilitydcat-ap_3.0.0_shacl_range.ttl` — Range constraints (`sh:class` / `sh:nodeKind`) for property values.
- `mobilitydcat-ap_3.0.0_shacl_mdr-vocabularies.shape.ttl` — Controlled-vocabulary (codelist) membership constraints.
- `mobilitydcat-ap_3.0.0_shacl_deprecateduris.ttl` — Warnings for deprecated mobilityDCAT-AP properties. DCAT-AP's own 2.x to 3.x deprecations are inherited via import, not restated here.
- `mobilitydcat-ap_3.0.0_shacl_imports.ttl` — Imports the DCAT-AP 3.0.1 SHACL shapes and other base ontologies.
- `mobilitydcat-ap_3.0.0_shacl_mdr_imports.ttl` — Imports the controlled-vocabulary codelists needed for validation.

## Severity levels

- `sh:Violation` — Mandatory properties. Must be fixed.
- `sh:Warning` — Recommended / deprecated properties. Should be addressed.
- `sh:Info` — Optional properties. May be added.

## Validation
For validation, see: **https://github.com/mobilityDCAT-AP/validation**

## Previous version
SHACL shapes for v1.1.0 are in `drafts/1.1.0-draft-0.1/shaclShapes`.
