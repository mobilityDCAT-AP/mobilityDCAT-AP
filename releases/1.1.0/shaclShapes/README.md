# mobilityDCAT-AP SHACL Shapes — v1.1.0

This directory contains the SHACL shapes for validating mobilityDCAT-AP 1.1.0 metadata.
All shapes extend and inherit from **DCAT-AP 2.0.1** SHACL shapes.

## Files

| File | Purpose |
|---|---|
| [`mobilitydcat-ap_1.1.0_shacl_shapes.ttl`](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/shaclShapes/mobilitydcat-ap_1.1.0_shacl_shapes.ttl) | Basic validation — cardinality, datatype, literal constraints |
| [`mobilitydcat-ap_1.1.0_shacl_range.ttl`](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/shaclShapes/mobilitydcat-ap_1.1.0_shacl_range.ttl) | Range validation — nodeKind and class membership for object properties |
| [`mobilitydcat-ap_1.1.0_shacl_mdr-vocabularies.shape.ttl`](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/shaclShapes/mobilitydcat-ap_1.1.0_shacl_mdr-vocabularies.shape.ttl) | Controlled vocabulary validation — property values must be from correct vocabularies per §5.2 |

## Inheritance

```
DCAT-AP 2.0.1 base shapes
        +
mobilityDCAT-AP 1.1.0 shacl_shapes.ttl                  (mobility structural extensions)
mobilityDCAT-AP 1.1.0 shacl_range.ttl                   (mobility range extensions)
mobilityDCAT-AP 1.1.0 shacl_mdr-vocabularies.shape.ttl  (mobility CV extensions)
```

## Validation toolkit

For Docker setup, Python scripts, and example test cases see:
**https://github.com/mobilityDCAT-AP/validation**


