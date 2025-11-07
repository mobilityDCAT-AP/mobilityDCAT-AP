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

## Credits

This SHACL validation setup builds upon the work by @MikiDi in [PR #129](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/pull/129).