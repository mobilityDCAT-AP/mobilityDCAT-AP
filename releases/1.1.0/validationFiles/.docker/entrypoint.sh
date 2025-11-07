#!/bin/bash

# Usage
if [ $# -ne 1 ]; then
    echo "Usage: $0 <your_rdf_file.rdf>" >&2
    exit 1
fi

MOBILITYDCAT_ENDPOINT="$1"

wget -q "$MOBILITYDCAT_ENDPOINT" -O /app/nap_dataset

cd /app/external_ontologies
for file in * ; do
    if [ -f "$file" ]; then
        rapper -i guess "$file" -o ntriples >> /app/combined.nt
    fi
done

cd /app
rapper -i guess /app/nap_dataset -o ntriples >> /app/combined.nt

pyshacl \
    -d \
    -s mobilitydcat-ap_shacl_shapes.ttl \
    -f turtle \
    -i none \
    /app/combined.nt
