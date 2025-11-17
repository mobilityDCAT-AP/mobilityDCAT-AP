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

```bash
cd validationFiles
docker build -f .docker/Dockerfile -t mobilitydcat-validator .
````

## Run Validation

```bash
docker run mobilitydcat-validator "https://transportdata.be/catalog.ttl"
```

### Validate local file

```bash
docker run -v $(pwd)/examples:/data mobilitydcat-validator /data/my-catalog.ttl
```

### Save validation report

```bash
docker run mobilitydcat-validator "https://example.com/catalog.ttl" > validation_report.ttl
```
