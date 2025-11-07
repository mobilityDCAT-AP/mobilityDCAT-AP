#!/bin/bash

set -e

# Usage
if [ $# -ne 1 ]; then
    echo "Usage: docker run mobilitydcat-validator <URL_or_FILE>" >&2
    echo ""
    echo "Examples:"
    echo "  docker run mobilitydcat-validator https://example.com/catalog.ttl"
    echo "  docker run -v /path/to/data:/data mobilitydcat-validator /data/catalog.ttl"
    exit 1
fi

INPUT="$1"

echo "================================================"
echo "mobilityDCAT-AP SHACL Validator"
echo "================================================"
echo "Input: $INPUT"
echo ""

# Download or copy input file
if [[ "$INPUT" =~ ^https?:// ]]; then
    echo "Downloading data from URL..."
    wget -q "$INPUT" -O /app/input_data.ttl
else
    echo "Using local file..."
    cp "$INPUT" /app/input_data.ttl
fi

# Combine external ontologies
echo "Combining external ontologies..."
cd /app/external_ontologies
for file in *.ttl *.rdf *.xml; do
    if [ -f "$file" ]; then
        rapper -i guess "$file" -o ntriples 2>/dev/null >> /app/combined.nt || true
    fi
done

# Add mobilityDCAT-AP ontology
cd /app
rapper -i guess mobilitydcat-ap.ttl -o ntriples 2>/dev/null >> /app/combined.nt || true

# Add input data
rapper -i guess /app/input_data.ttl -o ntriples 2>/dev/null >> /app/combined.nt || true

echo ""
echo "Running SHACL validation..."
echo "================================================"

# Run validation
pyshacl \
    -s mobilitydcat-ap_shacl_shapes.ttl \
    -f turtle \
    -i rdfs \
    /app/combined.nt

RESULT=$?

echo ""
echo "================================================"
if [ $RESULT -eq 0 ]; then
    echo "✓ Validation PASSED"
else
    echo "✗ Validation FAILED"
fi
echo "================================================"

exit $RESULT