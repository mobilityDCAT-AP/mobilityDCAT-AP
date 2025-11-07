#!/usr/bin/env python3
"""
Generate README.md from SHACL shapes and examples.
"""

import json
from pathlib import Path
from datetime import date

# Paths
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
SHAPES_DIR = PROJECT_ROOT / "shapes"
EXAMPLES_DIR = PROJECT_ROOT / "examples"
STATS_FILE = SHAPES_DIR / "shapes_statistics.json"
OUTPUT_README = PROJECT_ROOT / "README.md"

README_TEMPLATE = """# mobilityDCAT-AP SHACL Validation

**Last Updated:** {date}

## Overview

This directory contains SHACL shapes for validating mobilityDCAT-AP metadata. The shapes are organized into individual files for easier maintenance and can be automatically combined into a single validation file.

## Statistics

- **Total Shapes:** {total_shapes}
- **Total Properties:** {total_properties}
- **Mandatory Properties:** {mandatory_properties}

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
.venv\\Scripts\\Activate.ps1  # Windows PowerShell
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

{shapes_table}

## Development

### Setup
```bash
# Create virtual environment
uv venv

# Activate
.venv\\Scripts\\Activate.ps1  # Windows
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

## Shape Files

{shapes_details}

## Examples

{examples_section}

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

## License

Same as mobilityDCAT-AP - see root LICENSE file.

---

*This README is auto-generated. Do not edit manually - run `python scripts/generate_readme.py` instead.*
"""


def load_statistics():
    """Load statistics from JSON file."""
    if not STATS_FILE.exists():
        return None
    
    with open(STATS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_shapes_table(stats):
    """Generate markdown table of shapes."""
    if not stats:
        return "*Run `python scripts/combine_shapes.py` to generate statistics.*"
    
    table = "| Shape | File | Properties | Mandatory |\n"
    table += "|-------|------|------------|----------|\n"
    
    for shape in stats['shapes']:
        table += f"| **{shape['shape_name']}** | `{shape['file_name']}` | {shape['total_properties']} | {shape['mandatory_properties']} |\n"
    
    return table


def generate_shapes_details(stats):
    """Generate detailed shape descriptions."""
    if not stats:
        return "*Statistics not available yet.*"
    
    details = ""
    for shape in stats['shapes']:
        details += f"### {shape['shape_name']}\n\n"
        details += f"- **File:** `shapes/{shape['file_name']}`\n"
        details += f"- **Properties:** {shape['total_properties']}\n"
        details += f"- **Mandatory:** {shape['mandatory_properties']}\n"
        details += f"- **Size:** {shape['file_size_bytes']:,} bytes\n\n"
    
    return details


def generate_examples_section():
    """Generate examples section."""
    if not EXAMPLES_DIR.exists():
        return "*Example files coming soon.*"
    
    example_files = list(EXAMPLES_DIR.glob("*.ttl"))
    
    if not example_files:
        return "*No example files yet. Examples will be added for each shape.*"
    
    section = "| Example File | Description |\n"
    section += "|--------------|-------------|\n"
    
    for example in sorted(example_files):
        section += f"| `{example.name}` | Example for {example.stem} |\n"
    
    return section


def generate_readme():
    """Generate the README file."""
    
    print("Generating README...")
    
    # Load statistics
    stats = load_statistics()
    
    # Calculate totals
    total_shapes = len(stats['shapes']) if stats else 0
    total_properties = sum(s['total_properties'] for s in stats['shapes']) if stats else 0
    mandatory_properties = sum(s['mandatory_properties'] for s in stats['shapes']) if stats else 0
    
    # Generate sections
    shapes_table = generate_shapes_table(stats)
    shapes_details = generate_shapes_details(stats)
    examples_section = generate_examples_section()
    
    # Fill template
    readme_content = README_TEMPLATE.format(
        date=date.today().isoformat(),
        total_shapes=total_shapes,
        total_properties=total_properties,
        mandatory_properties=mandatory_properties,
        shapes_table=shapes_table,
        shapes_details=shapes_details,
        examples_section=examples_section
    )
    
    # Write README
    with open(OUTPUT_README, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ README generated: {OUTPUT_README}")
    print(f"  - {total_shapes} shapes documented")
    print(f"  - {total_properties} total properties")
    print(f"  - {mandatory_properties} mandatory properties")


if __name__ == "__main__":
    generate_readme()