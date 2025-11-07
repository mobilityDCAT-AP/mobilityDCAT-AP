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

Perfect — your `README.md` is already concise and functional.
Here’s how you can extend it **cleanly** with a `### 🧩 To-Do / Next Steps` section at the end, expressing that you plan to add more user-friendly, integrated examples for testing.

---

### ✅ Updated README.md (suggested version)

````markdown
## Build the Image
```bash
cd validationFiles
docker build -f .docker/Dockerfile -t mobilitydcat-validator .
````

## Run Validation

### ✅ Validate from URL

```bash
docker run mobilitydcat-validator "https://transportdata.be/catalog.ttl"
```

### ✅ Validate local file

```bash
docker run -v $(pwd)/examples:/data mobilitydcat-validator /data/my-catalog.ttl
```

### 💾 Save validation report

```bash
docker run mobilitydcat-validator "https://example.com/catalog.ttl" > validation_report.ttl
```

---

## 🧩 Credits

This SHACL validation setup builds upon the work by [@MikiDi](https://github.com/MikiDi) in PR [#129](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/pull/129).

---

## To-Do / Next Steps

* [ ] **Add more friendly, integrated examples**
  Include small, ready-to-run RDF examples (e.g. valid/invalid MobilityDCAT-AP catalogs) inside the `examples/` folder to make testing easier.
  Example goals:

  * Run validation directly with a sample RDF file.
  * Show what a passing and failing validation output looks like.
  * Demonstrate saving the report in Turtle and JSON-LD formats.

* [ ] **Provide example output snippets**
  Add sample console output and short explanation of typical validation messages.

* [ ] **Optional improvement**
  Include a `Makefile` or simple `validate.sh` script to wrap the Docker commands for smoother use.

