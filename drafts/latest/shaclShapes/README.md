# mobilityDCAT-AP SHACL Shapes (v3.0.0)

This directory contains the SHACL shapes for validating mobilityDCAT-AP v3.0.0 metadata.

## Files

- `mobilitydcat-ap-shacl.ttl` — Basic validation (cardinality, nodeKind, datatype, pattern checks). Extends DCAT-AP 3.0.1 SHACL via `owl:imports`.
- `mobilitydcat-ap-shacl-ranges.ttl` — Range constraints (`sh:class`). Extends DCAT-AP 3.0.1 range shapes via `owl:imports`.

## Usage

For basic validation only:
```
pyshacl -s mobilitydcat-ap-shacl.ttl -d your_metadata.ttl
```

For full validation (basic + range constraints):
```
pyshacl -s mobilitydcat-ap-shacl.ttl -e mobilitydcat-ap-shacl-ranges.ttl -d your_metadata.ttl
```

## Severity levels
- `sh:Violation` — Mandatory properties. Must be fixed.
- `sh:Warning` — Recommended properties. Should be added.
- `sh:Info` — Optional properties. May be added.

## Validation toolkit
For Docker setup, Python scripts, and test cases see:
**https://github.com/mobilityDCAT-AP/validation**

## Previous version
SHACL shapes for v1.1.0 are in `mobilityDCAT-AP\drafts\1.1.0-draft-0.1\shaclShapes`.