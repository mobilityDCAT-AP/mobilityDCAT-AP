# mobilityDCAT-AP SHACL Validation

**Last Updated:** 2025-11-07

## Overview

This directory contains SHACL shapes for validating mobilityDCAT-AP metadata. The shapes are organized into individual files for easier maintenance and can be automatically combined into a single validation file.

## Statistics

- **Total Shapes:** 10
- **Total Properties:** 19
- **Mandatory Properties:** 22

## Directory Structure
```
validationFiles/
├── shapes/                    # Individual SHACL shape files
├── scripts/                   # Automation scripts
│   ├── combine_shapes.py     # Combine shapes into one file
│   └── generate_readme.py    # Generate this README
├── .docker/                   # Docker validation setup
│   ├── Dockerfile
│   ├── entrypoint.sh
│   └── README.md
├── examples/                  # Example RDF files (coming soon)
└── mobilitydcat-ap_shacl_shapes.ttl  # Combined shapes file
```

## Quick Start

### 1. Combine Shapes
```bash
# Activate virtual environment
.venv\Scripts\Activate.ps1  # Windows PowerShell
source .venv/bin/activate      # Linux/Mac

# Combine all shapes
python scripts/combine_shapes.py
```

### 2. Docker Validation
```bash
# Build the validator
docker build -f .docker/Dockerfile -t mobilitydcat-validator .

# Validate from URL
docker run mobilitydcat-validator "https://example.com/catalog.ttl"

# Validate local file
docker run -v $(pwd)/examples:/data mobilitydcat-validator /data/your-file.ttl

# Save validation report
docker run mobilitydcat-validator "https://example.com/catalog.ttl" > report.ttl
```

## Available Shapes

| Shape | File | Properties | Mandatory |
|-------|------|------------|----------|
| **Address Agent Shape** | `Address_Agent_Shape.ttl` | 1 | 0 |
| **Agent Shape** | `Agent_Shape.ttl` | 9 | 1 |
| **Assessment Shape** | `Assessment_Shape.ttl` | 2 | 0 |
| **Catalog Record** | `Catalog_Record_shape.ttl` | 1 | 4 |
| **Catalogue Shape** | `Catalogue_Shape.ttl` | 1 | 7 |
| **Category Scheme** | `Category_Scheme_shape.ttl` | 1 | 1 |
| **Category** | `Category_shape.ttl` | 1 | 1 |
| **Checksum** | `Checksum_shape.ttl` | 1 | 2 |
| **Data Service** | `Data_Service_shape.ttl` | 1 | 2 |
| **Distribution** | `Distribution_shape.ttl` | 1 | 4 |


## Development

### Setup
```bash
# Create virtual environment
uv venv

# Activate
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # Linux/Mac

# Install dependencies
uv pip install -r requirements.txt
```

### Scripts

| Script | Purpose |
|--------|---------|
| `combine_shapes.py` | Combine individual shapes into one file |
| `generate_readme.py` | Generate this README automatically |

### Adding a New Shape

1. Create `shapes/YourClass_shape.ttl`
2. Follow the naming convention: `ClassName_shape.ttl`
3. Run `python scripts/combine_shapes.py`
4. Run `python scripts/generate_readme.py` to update docs

## 📚 Shape Files

### Address Agent Shape

- **File:** `shapes/Address_Agent_Shape.ttl`
- **Properties:** 1
- **Mandatory:** 0
- **Size:** 1,991 bytes

### Agent Shape

- **File:** `shapes/Agent_Shape.ttl`
- **Properties:** 9
- **Mandatory:** 1
- **Size:** 4,753 bytes

### Assessment Shape

- **File:** `shapes/Assessment_Shape.ttl`
- **Properties:** 2
- **Mandatory:** 0
- **Size:** 1,633 bytes

### Catalog Record

- **File:** `shapes/Catalog_Record_shape.ttl`
- **Properties:** 1
- **Mandatory:** 4
- **Size:** 3,118 bytes

### Catalogue Shape

- **File:** `shapes/Catalogue_Shape.ttl`
- **Properties:** 1
- **Mandatory:** 7
- **Size:** 6,641 bytes

### Category Scheme

- **File:** `shapes/Category_Scheme_shape.ttl`
- **Properties:** 1
- **Mandatory:** 1
- **Size:** 721 bytes

### Category

- **File:** `shapes/Category_shape.ttl`
- **Properties:** 1
- **Mandatory:** 1
- **Size:** 1,132 bytes

### Checksum

- **File:** `shapes/Checksum_shape.ttl`
- **Properties:** 1
- **Mandatory:** 2
- **Size:** 1,376 bytes

### Data Service

- **File:** `shapes/Data_Service_shape.ttl`
- **Properties:** 1
- **Mandatory:** 2
- **Size:** 2,777 bytes

### Distribution

- **File:** `shapes/Distribution_shape.ttl`
- **Properties:** 1
- **Mandatory:** 4
- **Size:** 7,360 bytes



## 🧪 Examples

*No example files yet. Examples will be added for each shape.*

## Validation Tips

### Common Issues

**Class Inheritance:**
- SHACL validators don't perform automatic reasoning
- Ensure ontologies are loaded (e.g., FOAF, DCAT)

**Controlled Vocabularies:**
- Use correct URI patterns from mobilityDCAT-AP vocabularies
- Check prefix declarations

### Recommended Validators

| Validator | Reasoning | Notes |
|-----------|-----------|-------|
| **pyshacl** | ✅ (with `-i rdfs`) | Recommended |
| **Docker** | ✅ | Pre-configured |
| **Apache Jena** | ⚠️ | Manual setup |

## Documentation

- [mobilityDCAT-AP Specification](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/)
- [SHACL Specification](https://www.w3.org/TR/shacl/)
- [Contributing Guide](../../CONTRIBUTING.md)

## Credits

This SHACL validation setup builds upon the work by @MikiDi in [PR #129](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/pull/129).

## License

Same as mobilityDCAT-AP - see root LICENSE file.

---

*This README is auto-generated. Do not edit manually - run `python scripts/generate_readme.py` instead.*
