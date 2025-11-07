# Docker-based SHACL Validation

## Build the Image
```bash
cd validationFiles
docker build -f .docker/Dockerfile -t mobilitydcat-validator .
```

## Run Validation

**Validate from URL:**
```bash
docker run mobilitydcat-validator "https://transportdata.be/catalog.ttl"
```

**Validate local file:**
```bash
docker run -v $(pwd)/examples:/data mobilitydcat-validator /data/my-catalog.ttl
```

**Save validation report:**
```bash
docker run mobilitydcat-validator "https://example.com/catalog.ttl" > validation_report.ttl
```

## What it does

1. Downloads all required ontologies and controlled vocabularies
2. Combines them with your data
3. Runs SHACL validation with RDFS reasoning
4. Outputs validation report in Turtle format